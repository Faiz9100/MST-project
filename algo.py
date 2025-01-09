import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MST Finder (Prim's & Kruskal's)")
        self.root.geometry("800x600")
        self.root.config(bg="#D8125B")  # Fuchsia background

        self.graph = []
        self.vertices = set()
        self.cycle_count = 0

        # Input Section
        frame = tk.Frame(self.root, padx=10, pady=10, bg="#D8125B", bd=2, highlightbackground="#2C2E39")
        frame.pack(pady=10)

        tk.Label(frame, text="From Vertex:", font=("Arial", 10), bg="#D8125B", fg="white").grid(row=0, column=0, padx=5)
        self.entry_from = tk.Entry(frame, width=5, font=("Arial", 10), bg="#D8125B", fg="white", insertbackground="white", bd=2, highlightbackground="#2C2E39")
        self.entry_from.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="To Vertex:", font=("Arial", 10), bg="#D8125B", fg="white").grid(row=0, column=2, padx=5)
        self.entry_to = tk.Entry(frame, width=5, font=("Arial", 10), bg="#D8125B", fg="white", insertbackground="white", bd=2, highlightbackground="#2C2E39")
        self.entry_to.grid(row=0, column=3, padx=5)

        tk.Label(frame, text="Weight:", font=("Arial", 10), bg="#D8125B", fg="white").grid(row=0, column=4, padx=5)
        self.entry_weight = tk.Entry(frame, width=5, font=("Arial", 10), bg="#D8125B", fg="white", insertbackground="white", bd=2, highlightbackground="#2C2E39")
        self.entry_weight.grid(row=0, column=5, padx=5)

        # Button styles with dark borders
        tk.Button(frame, text="Add Edge", command=self.add_edge, font=("Arial", 10), bg="#2C2E39", fg="white", bd=2, highlightbackground="#2C2E39").grid(row=0, column=6, padx=10)

        # Algorithm Buttons
        algorithm_frame = tk.Frame(self.root, bg="#D8125B", bd=2, highlightbackground="#2C2E39")
        algorithm_frame.pack(pady=10)

        tk.Button(algorithm_frame, text="Run Prim's Algorithm", command=self.run_prims, font=("Arial", 12), width=20, bg="#2C2E39", fg="white", bd=2, highlightbackground="#2C2E39").pack(pady=5)
        tk.Button(algorithm_frame, text="Run Kruskal's Algorithm", command=self.run_kruskal, font=("Arial", 12), width=20, bg="#2C2E39", fg="white", bd=2, highlightbackground="#2C2E39").pack(pady=5)

        # Output Section
        self.output_text = tk.Text(self.root, height=15, width=70, font=("Arial", 10), wrap=tk.WORD, bg="#2C2E39", fg="white", insertbackground="white", bd=2, highlightbackground="#2C2E39")
        self.output_text.pack(pady=10)

        # Clear Button with dark borders
        tk.Button(self.root, text="Clear Graph", command=self.clear_graph, font=("Arial", 12), width=20, bg="#2C2E39", fg="white", bd=2, highlightbackground="#2C2E39").pack(pady=5)

        # Graph Visualization
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(pady=10)

    def add_edge(self):
        """Add an edge to the graph."""
        try:
            u = int(self.entry_from.get())
            v = int(self.entry_to.get())
            weight = int(self.entry_weight.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for vertices and weight.")
            return

        self.graph.append([u, v, weight])
        self.vertices.update([u, v])
        self.output_text.insert(tk.END, f"Edge added: {u} --({weight})--> {v}\n")

        # Clear input fields
        self.entry_from.delete(0, tk.END)
        self.entry_to.delete(0, tk.END)
        self.entry_weight.delete(0, tk.END)

        self.update_graph_visualization()

    def run_prims(self):
        """Run Prim's algorithm."""
        if not self.graph:
            messagebox.showerror("Error", "Graph is empty! Add edges first.")
            return

        import heapq
        mst_weight = 0
        visited = set()
        adjacency_list = {v: [] for v in self.vertices}

        for u, v, weight in self.graph:
            adjacency_list[u].append((weight, v))
            adjacency_list[v].append((weight, u))

        min_heap = [(0, next(iter(self.vertices)))]  # Start from any vertex

        self.output_text.insert(tk.END, "\nRunning Prim's Algorithm:\n")
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            mst_weight += weight
            self.output_text.insert(tk.END, f"Visited {u}, Added weight: {weight}\n")

            for w, v in adjacency_list[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

        self.output_text.insert(tk.END, f"\nTotal Weight of MST (Prim's): {mst_weight}\n")

    def run_kruskal(self):
        """Run Kruskal's algorithm."""
        if not self.graph:
            messagebox.showerror("Error", "Graph is empty! Add edges first.")
            return

        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}
        self.cycle_count = 0

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                return False  # No cycle
            else:
                return True  # Cycle detected

        # Sort edges by weight
        self.graph.sort(key=lambda edge: edge[2])

        mst_weight = 0
        mst_edges = []

        self.output_text.insert(tk.END, "\nRunning Kruskal's Algorithm:\n")
        for u, v, weight in self.graph:
            if union(u, v):
                self.cycle_count += 1
            else:
                mst_edges.append((u, v, weight))
                mst_weight += weight
                self.output_text.insert(tk.END, f"Edge included: {u} --({weight})--> {v}\n")

        self.output_text.insert(tk.END, f"\nTotal Weight of MST (Kruskal's): {mst_weight}\n")
        self.output_text.insert(tk.END, f"Number of Cycles Detected: {self.cycle_count}\n")

    def clear_graph(self):
        """Clear the graph and the output."""
        self.graph.clear()
        self.vertices.clear()
        self.output_text.delete(1.0, tk.END)
        self.update_graph_visualization()

    def update_graph_visualization(self):
        """Update the graph visualization."""
        G = nx.Graph()
        G.add_weighted_edges_from(self.graph)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{w}" for u, v, w in self.graph}, ax=ax)

        self.canvas.draw()


# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()
