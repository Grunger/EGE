WHITE = 1
BLACK = 0


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        print('    castling left/right                -- рокировка с левой ил правой ладьёй')
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        elif 'move' in command:
            move_type, row, col, row1, col1 = command.split()
            row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
            if board.move_piece(row, col, row1, col1):
                print('Ход успешен')
                board.clear()
                board.attack_field_func()
                dan = board.danger()
                if dan == "мат":
                    if board.current_player_color() == WHITE:
                        print("\t   Game over\n\tЧерные победили!")
                        break
                    print("\t   Game over\n\tБелые победили!")
                    break
            else:
                print('Координаты некорректы! Попробуйте другой ход!')
        else:
            direct = command.split()[1]
            if board.current_player_color() == WHITE and board.get_piece(0, 4) == King and \
                    board.get_piece(0, 4).poss_cast:
                if direct == 'left' and board.get_piece(0, 0) == Rook and \
                        board.get_piece(0, 0).poss_cast:
                    board.castling(0, 4, 0, 2, 0, 0, 0, 3)
                elif direct == 'right' and board.get_piece(0, 7) == Rook and \
                        board.get_piece(0, 7).poss_cast:
                    board.castling(0, 4, 0, 6, 0, 7, 0, 5)
            elif board.current_player_color() == BLACK and board.get_piece(7, 4) == King and \
                    board.get_piece(7, 4).poss_cast:
                if direct == 'left' and board.get_piece(0, 0) == Rook and \
                        board.get_piece(0, 0).poss_cast:
                    board.castling(7, 4, 7, 2, 7, 0, 7, 3)
                elif direct == 'right' and board.get_piece(0, 7) == Rook and \
                        board.get_piece(0, 7).poss_cast:
                    board.castling(7, 4, 7, 6, 7, 7, 7, 5)


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        main_fig = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.field[1] = [Pawn(WHITE) for _ in range(8)]
        self.field[6] = [Pawn(BLACK) for _ in range(8)]
        self.field[0] = [main_fig[i](WHITE) for i in range(8)]
        self.field[7] = [main_fig[i](BLACK) for i in range(8)]
        self.attack_field = [[()] * 8 for _ in range(8)]
        self.ch = 0

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        return self.field[row][col]

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        dan = self.danger()
        if dan == "шах":
            self.ch = 1
        elif dan:
            return False
        else:
            self.ch = 0
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return
        if piece == Pawn and ((self.color == WHITE and row1 == 7) or
                              (self.color == BLACK and row1 == 0)):
            piece = piece.metamorphose()
        self.field[row][col] = None
        self.field[row1][col1] = piece
        self.color = opponent(self.color)
        return True

    def castling(self, kr, kc, kr1, kc1, rr, rc, rr1, rc1):
        self.field[kr][kc] = None
        self.field[kr1][kc1] = King
        self.field[rr][rc] = None
        self.field[rr1][rc1] = Rook

    def attack_field_func(self):
        for r in range(8):
            for c in range(8):
                if self.field[r][c] and self.field[r][c].get_color() != self.color:
                    self.attack_field = self.field[r][c].paint_field(self, self.attack_field, r, c)

    def clear(self):
        self.attack_field = [[()] * 8 for _ in range(8)]

    def danger(self):
        for i in self.field:
            for j in i:
                if j and j.get_type() == "King" and j.get_color() == self.color:
                    return j.danger(self, self.attack_field, self.ch)


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        pass

    def can_move(self, board, row, col, row1, col1):
        pass

    def correct_coords(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        pass

    def get_type(self):
        return None


class Queen(Figure):
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if not self.correct_coords(row, col):
            return False

        if abs(row - row1) != abs(col - col1) and row != row1 and col != col1:
            return False
        if row != row1 and col != col1:
            step = 1 if (row1 >= row) else -1
            step2 = 1 if (col1 >= col) else -1
            c = col
            for r in range(row + step, row1, step):
                c += step2
                if not (board.get_piece(r, c) is None):
                    return False
        else:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False

            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        rz = r
        cz = c
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                r = rz
                c = cz
                while True:
                    r += i
                    c += j
                    if not self.correct_coords(r, c):
                        break
                    elif not (board.get_piece(r, c) is None):
                        if board.get_piece(r, c).get_color() != self.color:
                            attack_field[r][c] += (1,)
                        break
                    attack_field[r][c] += (1,)
        c = cz
        for i in range(-1, 2, 2):
            r = rz
            while True:
                r += i
                if not self.correct_coords(r, c):
                    break
                elif not (board.get_piece(r, c) is None):
                    if board.get_piece(r, c).get_color() != self.color:
                        attack_field[r][c] += (1,)
                    break
                attack_field[r][c] += (1,)
        r = rz
        for i in range(-1, 2, 2):
            c = cz
            while True:
                c += i
                if not self.correct_coords(r, c):
                    break
                elif not (board.get_piece(r, c) is None):
                    if board.get_piece(r, c).get_color() != self.color:
                        attack_field[r][c] += (1,)
                    break
                attack_field[r][c] += (1,)
        return attack_field


class Pawn(Figure):
    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1 or row == row1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if row == start_row and row + 2 * direction == row1:
            return True

        return False

    def metamorphose(self):
        print("Выберите новую фигуру:")
        print("1) слон")
        print("2) конь")
        print("3) ладья")
        print("4) ферзь")
        chouse = int(input())
        if chouse == 1:
            return Bishop(self.color)
        elif chouse == 2:
            return Knight(self.color)
        elif chouse == 3:
            return Rook(self.color)
        else:
            return Queen(self.color)

    def can_attack(self, board, row, col, row1, col1):
        if col == col1 or row == row1:
            return False

        if self.color == WHITE:
            direction = 1
        else:
            direction = -1

        if row + direction == row1 and abs(col - col1) == 1:
            return True

        return False

    def paint_field(self, board, attack_field, r, c):
        if self.color == BLACK:
            if c == 0:
                attack_field[r - 1][c + 1] += (5,)
            elif c == 7:
                attack_field[r - 1][c - 1] += (5,)
            elif r != 0:
                attack_field[r - 1][c - 1] += (5,)
                attack_field[r - 1][c + 1] += (5,)
        else:
            if c == 0:
                attack_field[r + 1][c + 1] += (5,)
            elif c == 7:
                attack_field[r + 1][c - 1] += (5,)
            elif r != 7:
                attack_field[r + 1][c - 1] += (5,)
                attack_field[r + 1][c + 1] += (5,)
        return attack_field


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.poss_cast = True

    def char(self):
        return "R"

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        self.poss_cast = False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        rz = r
        cz = c
        for i in range(-1, 2, 2):
            r = rz
            while True:
                r += i
                if not self.correct_coords(r, c):
                    break
                elif not (board.get_piece(r, c) is None):
                    if board.get_piece(r, c).get_color() != self.color:
                        attack_field[r][c] += (4,)
                    break
                attack_field[r][c] += (4,)
        r = rz
        for i in range(-1, 2, 2):
            c = cz
            while True:
                c += i
                if not self.correct_coords(r, c):
                    break
                elif not (board.get_piece(r, c) is None):
                    if board.get_piece(r, c).get_color() != self.color:
                        attack_field[r][c] += (4,)
                    break
                attack_field[r][c] += (4,)
        return attack_field


class Knight(Figure):
    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        if not self.correct_coords(row, col):
            return False
        if (abs(row1 - row) == 1 and abs(col1 - col) == 2) or (abs(
                row1 - row) == 2 and abs(col1 - col) == 1):
            return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) - abs(j) == 0 or i == 0 or j == 0:
                    continue
                if self.correct_coords(r + i, c + j):
                    attack_field[r + i][c + j] += (3,)
        return attack_field


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if not self.correct_coords(row, col):
            return False
        if abs(col - col1) == abs(row - row1):
            return True

        step = 1 if (row1 >= row) else -1
        step2 = 1 if (col1 >= col) else -1
        c = col
        for r in range(row + step, row1, step):
            c += step2
            if not (board.get_piece(r, c) is None):
                return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        rz = r
        cz = c
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                r = rz
                c = cz
                while True:
                    r += i
                    c += j
                    if not self.correct_coords(r, c):
                        break
                    elif not (board.get_piece(r, c) is None):
                        if board.get_piece(r, c).get_color() != self.color:
                            attack_field[r][c] += (2,)
                        break
                    attack_field[r][c] += (2,)
        return attack_field


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.poss_cast = True
        if self.color == WHITE:
            self.coords = (0, 4)
        else:
            self.coords = (7, 4)

    def char(self):
        return "K"

    def can_move(self, board, row, col, row1, col1):
        self.poss_cast = False
        if not self.correct_coords(row, col):
            return False
        if abs(row - row) != 1 and abs(col - col) != 1:
            return False
        else:
            self.coords = (row1, col1)
            return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def paint_field(self, board, attack_field, r, c):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not self.correct_coords(r + i, c + j):
                    break
                elif not (board.get_piece(r + i, c + j) is None):
                    break
                attack_field[r + i][c + j] += (0,)
        return attack_field

    def danger(self, board, attack_field, ch):
        r = self.coords[0]
        c = self.coords[1]
        if ch == 1 and attack_field[r, c] != ():
            return True
        if attack_field[r][c] != ():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self.correct_coords(r + i, c + j) and \
                            attack_field[r + i][c + j] == () and \
                            board.get_piece(r + i, c + j) is None:
                        return "шах"
            return "мат"
        return False

    def get_type(self):
        return "King"


if __name__ == '__main__':
    main()
