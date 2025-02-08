import tkinter as tk
from tkinter import ttk
from .utils import ALGORITHMS


class AlgorithmVisualizer:
    
    def __init__(self):
        
        self.selected_algorithm = None
        self.window_count = 0

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
        ttk.Label(self.main_frame, text="Algorithm Visualizer", style="Title.TLabel").pack(anchor="w")

        # Tree Frame
        self.tree_frame = tk.Frame(self.main_frame, bg="#303030")
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Treeview
        self.tree = ttk.Treeview(self.tree_frame, style="Treeview")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree["show"] = "tree"
        
        self.tree.bind("<<TreeviewSelect>>", self.on_algorithm_selected)
        
        self.create_menu()

        self.tree.selection_set(self.tree.get_children()[0])
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

    def create_menu(self):
        categories = {}

        for algo_data in ALGORITHMS.values():
            category = algo_data["type"]
            if category not in categories:
                categories[category] = self.tree.insert("", "end", text=category, open=False)

        for algo_name, algo_data in ALGORITHMS.items():
            category_id = categories[algo_data["type"]]
            self.tree.insert(category_id, "end", text=algo_name)
            
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
            algo_data = ALGORITHMS.get(self.selected_algorithm)
            if algo_data:
                self.window_count += 1
                window_class = algo_data["window_class"]
                window_class(self.root, self.selected_algorithm, self.window_count)

    def run(self):
        self.root.mainloop()
    