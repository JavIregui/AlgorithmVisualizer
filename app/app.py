import tkinter as tk
from tkinter import ttk


################################
# Función print nombre algoritmo seleccionado
# Función abre nueva ventana con el algoritmo seleccionado
################################


class AlgorithmVisualizer:
    def __init__(self):
        
        self.selected_algorithm = None

        # Window
        self.root = tk.Tk()
        self.root.title("Algorithm Visualizer")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#303030")

        # Styles
        self.create_theme()
        style = ttk.Style()
        style.theme_use("myTheme")

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="#303030")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)

        # Label
        ttk.Label(self.main_frame, text="Algorithms", style="Title.TLabel").pack(anchor="w")

        # Tree Frame
        self.tree_frame = tk.Frame(self.main_frame, bg="#303030")
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Treeview
        self.tree = ttk.Treeview(self.tree_frame, style="Treeview")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree["show"] = "tree"

        sorting_id = self.tree.insert("", "end", text="Sorting algorithms", open=False)
        searching_id = self.tree.insert("", "end", text="Search algorithms", open=False)
        graph_id = self.tree.insert("", "end", text="Graph algorithms", open=False)
        backtracking_id = self.tree.insert("", "end", text="Backtracking algorithms", open=False)
        maze_id = self.tree.insert("", "end", text="Maze generation algorithms", open=False)
        evolution_id = self.tree.insert("", "end", text="Evolutionary algorithms", open=False)
        geometric_id = self.tree.insert("", "end", text="Geometric algorithms", open=False)
        
        # Adding items to the tree
        self.tree.insert(sorting_id, "end", text="Bubble Sort")
        self.tree.insert(sorting_id, "end", text="Selection Sort")
        self.tree.insert(sorting_id, "end", text="Insertion Sort")
        self.tree.insert(sorting_id, "end", text="Merge Sort")
        self.tree.insert(sorting_id, "end", text="Quick Sort")
        self.tree.insert(sorting_id, "end", text="Heap Sort")
        self.tree.insert(sorting_id, "end", text="Radix Sort")
        self.tree.insert(sorting_id, "end", text="Counting Sort")
        self.tree.insert(sorting_id, "end", text="Shell Sort")
        self.tree.insert(sorting_id, "end", text="Cocktail Shaker Sort")
        self.tree.insert(sorting_id, "end", text="Tim Sort")
        self.tree.insert(sorting_id, "end", text="Gnome Sort")
        
        self.tree.insert(searching_id, "end", text="Linear Search")
        self.tree.insert(searching_id, "end", text="Binary Search")
        self.tree.insert(searching_id, "end", text="Jump Search")
        self.tree.insert(searching_id, "end", text="Exponential Search")
        self.tree.insert(searching_id, "end", text="Interpolation Search")
        self.tree.insert(searching_id, "end", text="Ternary Search")
        self.tree.insert(searching_id, "end", text="Fibonacci Search")
        
        self.tree.insert(graph_id, "end", text="Dijkstra")
        self.tree.insert(graph_id, "end", text="A*")
        self.tree.insert(graph_id, "end", text="Breadth-First Search (BFS)")
        self.tree.insert(graph_id, "end", text="Depth-First Search (DFS)")
        
        self.tree.insert(backtracking_id, "end", text="N Queen Problem")
        self.tree.insert(backtracking_id, "end", text="Sudoku Solver")
        self.tree.insert(backtracking_id, "end", text="Knight's Tour")
        
        self.tree.insert(maze_id, "end", text="Recursive Backtracking")
        self.tree.insert(maze_id, "end", text="Prim's Algorithm")
        self.tree.insert(maze_id, "end", text="Kruskal's Algorithm")
        
        self.tree.insert(evolution_id, "end", text="Genetic Algorithm")
        
        self.tree.insert(geometric_id, "end", text="Convex Hull (Graham's Algorithm)")

        self.tree.selection_set(sorting_id)
        self.tree.focus_force()

        # Scrollbar
        
        tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical",
                                    command=self.tree.yview, style="Vertical.TScrollbar")
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        # Creates the custom ScrollBar
        self.thumb_img = tk.PhotoImage(width=1, height=1)
        self.thumb_img.put("#404040", to=(0, 0, 1, 1))
        self.trough_img = tk.PhotoImage(width=10, height=1)
        self.trough_img.put("#505050", to=(0, 0, 10, 1))
        
        style.tk.call("ttk::style", "element", "create", "Flat.Scrollbar.thumb", "image", self.thumb_img,
                      "-border", "0", "-sticky", "nswe")
        style.tk.call("ttk::style", "element", "create", "Flat.Scrollbar.trough", "image", self.trough_img,
                      "-border", "0", "-sticky", "ns")
        
        style.layout("Vertical.TScrollbar", [
            ('Flat.Scrollbar.trough', {
                'sticky': 'ns',
                'children': [
                    ('Flat.Scrollbar.thumb', {'sticky': 'nswe'})
                ]
            })
        ])

        # Play Button
        ttk.Button(self.main_frame, text="Run Algorithm", style="Play.TButton").pack(fill=tk.X)

    def create_theme(self):
        style = ttk.Style()
        if "myTheme" not in style.theme_names():
            style.theme_create("myTheme", parent="default", settings={
                "Treeview": {
                    "configure": {"background": "#404040", "foreground": "#FFFFFF", "fieldbackground": "#404040", "borderwidth": 0, "padding": (5, 5), "focuscolor": "#404040", "focusthickness": 0},
                    "map": {"background": [("selected", "#505050")], "foreground": [("selected", "#FFFFFF")]}
                },
                "Vertical.TScrollbar": {
                    "configure": {"background": "#505050", "troughcolor": "#404040", "arrowcolor": "#404040", "borderwidth": 0, "relief": "flat", "gripcount": 0, "elementborderwidth": 0},
                    "map": {"background": [("active", "#505050")]}
                },
                "Play.TButton": {
                    "configure": {"font": ("Helvetica", 12), "background": "#404040", "foreground": "#FFFFFF", "borderwidth": 0, "relief": "flat", "anchor": "center", "padding": (10, 5)},
                    "map": {"background": [("active", "#505050"), ("focus", "#505050")]}
                },
                "Title.TLabel": {
                    "configure": {"background": "#303030", "foreground": "#FFFFFF", "font": ("Helvetica", 16)}
                },
            })

    def run(self):
        self.root.mainloop()