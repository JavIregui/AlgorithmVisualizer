import tkinter as tk
from tkinter import ttk


################################
# ARREGLAR ESTILOS DE SCROLLBAR
# Añadir lista algoritmos
# Función print nombre algoritmo seleccionado
# Función abre nueva ventana con el algoritmo seleccionado
################################


class AlgorithmVisualizer:
    def __init__(self):
        
        self.selected_algorithm = None

        # Window
        self.root = tk.Tk()
        self.root.title("Algorithm Visualizer")
        self.root.geometry("400x350")
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

        sorting_id = self.tree.insert("", "end", text="Ordenamiento", open=True)
        searching_id = self.tree.insert("", "end", text="Búsqueda", open=True)

        for _ in range(10):  # Insertar 10 veces cada búsqueda
            self.tree.insert(sorting_id, "end", text="Bubble Sort")
            self.tree.insert(sorting_id, "end", text="Merge Sort")
            self.tree.insert(sorting_id, "end", text="Quick Sort")
            self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
            self.tree.insert(searching_id, "end", text="Búsqueda Binaria")

        self.tree.selection_set(sorting_id)
        self.tree.focus_force()

        # Scrollbar
        tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview, style="Treeview.Vertical.TScrollbar")
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Play Button
        ttk.Button(self.main_frame, text="Run Algorithm", style="Play.TButton").pack(fill=tk.X)

    def create_theme(self):
        style = ttk.Style()
        if "myTheme" not in style.theme_names():
            style.theme_create("myTheme", parent="default", settings={
                "Treeview": {
                    "configure": {"background": "#404040", "foreground": "#FFFFFF", "fieldbackground": "#404040", "borderwidth": 0},
                    "map": {"background": [("selected", "#505050")], "foreground": [("selected", "#FFFFFF")]}
                },
                "Treeview.Vertical.TScrollbar": {
                    "configure": {"background": "#505050", "troughcolor": "#303030", "borderwidth": 0, "relief": "flat", "elementborderwidth": 0}
                },
                "Play.TButton": {
                    "configure": {"font": ("Helvetica", 14), "background": "#404040", "foreground": "#FFFFFF", "borderwidth": 0, "relief": "flat"},
                    "map": {"background": [("active", "#505050"), ("focus", "#505050")]}
                },
                "Title.TLabel": {
                    "configure": {"background": "#303030", "foreground": "#FFFFFF", "font": ("Helvetica", 18)}
                }
            })

    def run(self):
        self.root.mainloop()