import random


def generate_dag(num_vertices, num_edges, max_vertex_id=1000, max_weight=10000):
    if num_edges > num_vertices * (num_vertices - 1) // 2:
        raise ValueError("Слишком много рёбер для ациклического графа")

    vertices = random.sample(range(1, max_vertex_id + 1), num_vertices)

    edges = set()
    while len(edges) < num_edges:
        i = random.randint(0, num_vertices - 2)
        j = random.randint(i + 1, num_vertices - 1)
        u, v = vertices[i], vertices[j]
        w = round(random.uniform(0.001, max_weight), 3)
        edges.add((u, v, w))

    return list(edges), vertices


def write_graph_to_file(edges, filename):
    with open(filename, 'w') as f:
        for u, v, w in edges:
            f.write(f"{u}\t{v}\t{w}\n")


def find_sources_sinks(edges, vertices):
    outgoing = {v: set() for v in vertices}
    incoming = {v: set() for v in vertices}

    for u, v, _ in edges:
        outgoing[u].add(v)
        incoming[v].add(u)

    sources = [v for v in vertices if len(incoming[v]) == 0]
    sinks = [v for v in vertices if len(outgoing[v]) == 0]

    return sorted(sources), sorted(sinks)


if __name__ == "__main__":
    n_vertices = int(input("Количество вершин: "))
    n_edges = int(input("Количество рёбер: "))

    try:
        graph_edges, all_vertices = generate_dag(n_vertices, n_edges)
        write_graph_to_file(graph_edges, "graph.txt")

        sources, sinks = find_sources_sinks(graph_edges, all_vertices)

        print(f"Граф успешно сгенерирован и сохранён в graph.txt ({len(graph_edges)} рёбер)")
        print(f"Истоки (нет входящих рёбер): {sources}")
        print(f"Стоки (нет исходящих рёбер): {sinks}")
    except ValueError as e:
        print(f"Ошибка: {e}")
