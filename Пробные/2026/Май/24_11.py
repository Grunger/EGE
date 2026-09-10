def is_hex_digit(c):
    """Проверяет, является ли символ 16‑ричной цифрой."""
    return c in '0123456789ABCDEF'

def is_even_hex(c):
    """Проверяет, чётная ли 16‑ричная цифра."""
    return c in '02468ACE'

# Читаем файл
with open('1_24.txt', 'r') as f:
    s = f.readline().strip()

max_length = 0
current_seq = ''

for char in s:
    if is_hex_digit(char):
        current_seq += char
    else:
        # Конец последовательности 16‑ричных цифр — анализируем её
        if current_seq:
            # Ищем все значащие подстроки внутри текущей последовательности
            for start in range(len(current_seq)):
                if current_seq[start] != '0':  # Начинается не с нуля
                    substring = current_seq[start:]
                    if is_even_hex(substring[-1]):  # Оканчивается на чётную цифру
                        max_length = max(max_length, len(substring))
        current_seq = ''  # Сбрасываем последовательность

# Проверяем последнюю последовательность (если файл не заканчивается не‑16‑ричным символом)
if current_seq:
    for start in range(len(current_seq)):
        if current_seq[start] != '0':
            substring = current_seq[start:]
            if is_even_hex(substring[-1]):
                max_length = max(max_length, len(substring))

print(max_length)
