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
        style = ttk.Style()
        style.theme_use("default")
        
        style.configure("tree.Treeview", background="#404040", foreground="#FFFFFF", fieldbackground="#404040", borderwidth=0)
        style.map("tree.Treeview", background=[("selected", "#505050")], foreground=[("selected", "#FFFFFF")])
        
        style.configure("Play.TButton", font=("Helvetica", 14), background="#404040", foreground="#FFFFFF", borderwidth=0, relief="flat")
        style.map("Play.TButton", background=[("active", "#505050"), ("focus", "#505050")])

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="#303030")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)

        # Label
        self.title_label = tk.Label(self.main_frame, text="Algorithms", bg="#303030", fg="#FFFFFF", font=("Helvetica", 18))
        self.title_label.pack(anchor="w")

        # Tree Frame
        self.tree_frame = tk.Frame(self.main_frame, bg="#303030")
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Treeview
        self.tree = ttk.Treeview(self.tree_frame, style="tree.Treeview")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree["show"] = "tree"

        sorting_id = self.tree.insert("", "end", text="Ordenamiento", open=True)
        searching_id = self.tree.insert("", "end", text="Búsqueda", open=True)

        self.tree.insert(sorting_id, "end", text="Bubble Sort")
        self.tree.insert(sorting_id, "end", text="Merge Sort")
        self.tree.insert(sorting_id, "end", text="Quick Sort")

        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")
        self.tree.insert(searching_id, "end", text="Búsqueda Lineal")
        self.tree.insert(searching_id, "end", text="Búsqueda Binaria")

        self.tree.selection_set(sorting_id)
        self.tree.focus_force()
        
        # Scrollbar
        self.tree_scroll = tk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_scroll.configure(bg="#505050", troughcolor="#303030", bd=0, relief="flat", elementborderwidth=0)

        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        # Play Button
        self.play_button = ttk.Button(self.main_frame, text="Run Algorithm", style="Play.TButton")
        self.play_button.pack(fill=tk.X)


    def run(self):
        self.root.mainloop()