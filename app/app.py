import tkinter as tk
from tkinter import ttk


################################
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
        
        self.tree.bind("<<TreeviewSelect>>", self.on_algorithm_selected)

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
        ttk.Button(self.main_frame, text="Run Algorithm", style="Play.TButton", command=self.run_algorithm).pack(fill=tk.X)

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

    def on_algorithm_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            parent_id = self.tree.parent(item_id)

            if parent_id:
                self.selected_algorithm = self.tree.item(item_id, "text")
            else:
                self.selected_algorithm = None
            
    def run_algorithm(self):
        if self.selected_algorithm:
            # Crear la nueva ventana
            self.algorithm_window = tk.Toplevel(self.root)
            self.algorithm_window.title(self.selected_algorithm)

            # Obtener dimensiones de la pantalla y de la ventana principal
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            menu_x = self.root.winfo_x()
            menu_y = self.root.winfo_y()
            menu_width = self.root.winfo_width()
            menu_height = self.root.winfo_height()

            # Definir tamaño de la nueva ventana
            win_width, win_height = 600, 400  # Tamaño fijo o dinámico según el contenido

            # Buscar una posición libre en la pantalla
            if menu_x + menu_width + win_width < screen_width:  # A la derecha si cabe
                win_x = menu_x + menu_width + 10
                win_y = menu_y
            elif menu_y + menu_height + win_height < screen_height:  # Debajo si cabe
                win_x = menu_x
                win_y = menu_y + menu_height + 10
            else:  # Si no hay espacio, centrar la ventana en la pantalla
                win_x = (screen_width - win_width) // 2
                win_y = (screen_height - win_height) // 2

            # Posicionar la ventana
            self.algorithm_window.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

            # Contenido de prueba
            label = tk.Label(self.algorithm_window, text=f"Running {self.selected_algorithm}...", font=("Arial", 16))
            label.pack(pady=20)
    
    def run(self):
        self.root.mainloop()