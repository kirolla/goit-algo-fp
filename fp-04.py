import matplotlib.pyplot as plt
import networkx as nx
import uuid

# Клас, що представляє вузол дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

# Клас, що представляє бінарну купу
class Heap:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            self.build(values)

    # Побудова бінарної купи зі списку значень
    def build(self, values):
        for value in values:
            self.insert(value)

    # Вставка значення в купу
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = Node(value)
                    break
                else:
                    queue.append(current.left)
                if not current.right:
                    current.right = Node(value)
                    break
                else:
                    queue.append(current.right)

# Клас для візуалізації дерева
class TreeVis:
    # Статичний метод для візуалізації дерева
    def visualize_heap(self, heap):
        graph = nx.DiGraph()
        pos = {}
        TreeVis.build_graph(heap.root, graph, pos)
        labels = {node: data["label"] for node, data in graph.nodes(data=True)}

        # Візуалізація графа
        plt.figure(figsize=(8, 5))
        nx.draw(
            graph,
            pos=pos,
            labels=labels,
            with_labels=True,
            arrows=False,
            node_size=2500,
        )
        plt.show()

    # Статичний метод для побудови графа дерева
    def build_graph(node, graph=None, pos={}, x=0, y=0, layer=0):
        if node is not None:
            graph.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)
            layer_gap = 1 / (2 ** (layer + 1))
            if node.left:
                graph.add_edge(node.id, node.left.id)
                TreeVis.build_graph(
                    node.left, graph, pos, x=x - layer_gap, y=y - 1, layer=layer + 1
                )
            if node.right:
                graph.add_edge(node.id, node.right.id)
                TreeVis.build_graph(
                    node.right, graph, pos, x=x + layer_gap, y=y - 1, layer=layer + 1
                )
        return graph, pos

# Головна функція для запуску програми
def main():
    values = [1, 3, 2, 7, 6, 4, 5]
    heap = Heap(values)
    tree_visualizer = TreeVis()
    tree_visualizer.visualize_heap(heap)

# Виклик головної функції при запуску скрипту
if __name__ == "__main__":
    main()
