"""
Пример работы с библиотекой NetworkX
"""
import matplotlib.pyplot as plt
import networkx as nx

# Создание пустого графа
graph = nx.Graph()

# Добавление вершин
graph.add_node("A")
graph.add_nodes_from(["B", "C", "D"])

# Установка координат для вершин
set_coordinates = {"A": (0, 0), "B": (1, 1), "C": (2, 2), "D": (1, -1)}

# Добавление рёбер
graph.add_edge("A", "B")
graph.add_edges_from([("B", "C"), ("C", "D"), ("D", "A")])

# Получение списка вершин и рёбер
nodes = graph.nodes()
edges = graph.edges()

# Визуализация графа
nx.draw(graph, pos=set_coordinates, with_labels=True, node_color='red', edge_color='green')
plt.show()

"""
Пример работы с библиотекой igraph
"""
# import igraph as ig
#
# # Создание пустого графа
# graph = ig.Graph()
#
# # Добавление вершин
# graph.add_vertices(4)
#
# # Добавление рёбер
# graph.add_edges([(0, 1), (1, 2), (2, 3), (3, 0)])
#
# # Получение списка вершин и рёбер
# nodes = graph.vs
# edges = graph.es
#
# # Визуализация графа
# layout = graph.layout('circle')
# ig.plot(graph, layout=layout, vertex_color='lightblue', edge_color='gray')
# input()