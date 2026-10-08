import math

def read_points(filename):
    with open(filename, 'r') as f:
        return [tuple(map(float, line.replace(',', '.').strip().split())) for line in f]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def manhattan_distance_x(p1, p2):
    return abs(p1[0] - p2[0])

def manhattan_distance_y(p1, p2):
    return abs(p1[1] - p2[1])

def center_of_cluster(cluster):
    min_sum = float('inf')
    center = None
    for p in cluster:
        total = sum(distance(p, q) for q in cluster)
        if total < min_sum:
            min_sum = total
            center = p
    return center

def max_axis_distances(cluster, center):
    max_dx = max(manhattan_distance_x(center, p) for p in cluster)
    max_dy = max(manhattan_distance_y(center, p) for p in cluster)
    return max_dx, max_dy

def classify_a(points):
    clusters = [[] for _ in range(2)]
    for x, y in points:
        if y < 2 - x ** 2 and x > 0 and y > x:  # Под параболой, над прямой y = x и левее оси Y
            clusters[0].append((x, y))
        elif y > x and y < 0 and y < 2 - x ** 2:  # Под параболой, над прямой y = x и нижу оси X
            clusters[1].append((x, y))
        # Остальные считаются аномалиями
    return clusters

def classify_b(points):
    clusters = [[] for _ in range(4)]
    for x, y in points:
        if x ** 2 + y ** 2 < 1 and y > 0 and x < 0:
            clusters[0].append((x, y))  # Внутри круга слева сверху
        elif x ** 2 + y ** 2 > 1 and y < 1 and y > x - 1 and x > 0 and y > 0:
            clusters[1].append((x, y))  # Вне круга справа сверху
        elif x ** 2 + y ** 2 > 1 and y > x - 1 and x < 0 and y < 0:
            clusters[2].append((x, y))  # Вне круга слева снизу
        elif y < x - 1 and x ** 2 + y ** 2 < 1 and y < 0 and x > 0:
            clusters[3].append((x, y))  # Внутри круга справа снизу
        # Остальные считаются аномалиями
    return clusters

def analyze(points, classifier):
    clusters = classifier(points)
    px = 0
    py = 0
    for cluster in clusters:
        if len(cluster) == 0:
            continue
        center = center_of_cluster(cluster)
        dx, dy = max_axis_distances(cluster, center)
        px = max(px, dx)
        py = max(py, dy)
    return int(px * 10000), int(py * 10000)

# Чтение точек
points_a = read_points("27-А.txt")
#points_b = read_points("27-Б.txt")

# Анализ
px_a, py_a = analyze(points_a, classify_a)
#px_b, py_b = analyze(points_b, classify_b)

# Вывод
print(px_a, py_a)
#print(px_b, py_b)