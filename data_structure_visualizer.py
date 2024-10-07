import networkx as nx
import matplotlib.pyplot as plt

class DataStructureVisualizer:
    def __init__(self):
        self.graph = nx.Graph()
        self.node_counter = 0

    def add_node(self, label):
        self.node_counter += 1
        self.graph.add_node(self.node_counter, label=label)
        print(f"Node {label} added with ID {self.node_counter}")
        self.visualize_graph()

    def add_edge(self, node1_id, node2_id):
        if node1_id in self.graph.nodes and node2_id in self.graph.nodes:
            self.graph.add_edge(node1_id, node2_id)
            print(f"Edge added between Node {node1_id} and Node {node2_id}")
            self.visualize_graph()
        else:
            print("One or both nodes do not exist.")

    def remove_node(self, node_id):
        if node_id in self.graph.nodes:
            self.graph.remove_node(node_id)
            print(f"Node {node_id} removed.")
            self.visualize_graph()
        else:
            print("Node does not exist.")

    def remove_edge(self, node1_id, node2_id):
        if self.graph.has_edge(node1_id, node2_id):
            self.graph.remove_edge(node1_id, node2_id)
            print(f"Edge removed between Node {node1_id} and Node {node2_id}")
            self.visualize_graph()
        else:
            print("Edge does not exist.")

    def visualize_graph(self):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'label')
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold")
        plt.show()

# Example Usage
visualizer = DataStructureVisualizer()
visualizer.add_node("A")
visualizer.add_node("B")
visualizer.add_edge(1, 2)
visualizer.remove_edge(1, 2)
visualizer.remove_node(1)
