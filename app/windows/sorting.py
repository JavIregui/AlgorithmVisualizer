import tkinter as tk
from tkinter import ttk
import time

from .utils import calculate_window_position

class SortingWindow:
    def __init__(self, root, algorithm_name, offset):
        
        # Window
        self.window = tk.Toplevel(root)
        self.window.title(algorithm_name)
        self.window.resizable(False, False)
        self.window.configure(bg="#303030")
        
        self.win_width = 600
        self.win_height = 400
        
        self.win_x, self.win_y = calculate_window_position(root, self.win_width, self.win_height, offset)

        self.window.geometry(f"{self.win_width}x{self.win_height}+{self.win_x}+{self.win_y}")
        
        # Styles
        self.create_theme()
        style = ttk.Style()
        style.theme_use("myTheme")

        # Main Frame
        self.frame = tk.Frame(self.window, bg="#303030")
        self.frame.pack(fill=tk.X, padx=25, pady=20)
        
        # Label
        ttk.Label(self.frame, text=algorithm_name, style="Title.TLabel").pack(side=tk.LEFT)
        
        # Learn more button
        ttk.Button(self.frame, text="Learn more", style="Play.TButton", command=self.show_algorithm_info).pack(side=tk.LEFT, padx=20)
        
        # Item counter
        self.n = tk.StringVar(value="15")
        self.n.trace_add("write", self.validate_n)
        
        self.item_count_entry = tk.Entry(self.frame, font=("Helvetica", 12), width=5, textvariable=self.n)
        self.item_count_entry.pack(side=tk.RIGHT)
        tk.Label(self.frame, text="n:", font=("Helvetica", 12), fg="#FFFFFF", bg="#303030").pack(side=tk.RIGHT, padx=10)
        
        # Canvas
        self.canvas = tk.Canvas(self.window, bg="#404040")
        self.canvas.pack(fill=tk.BOTH, padx=25, expand=True)
        
        # Frame inferior con temporizador y botón play/stop
        bottom_frame = tk.Frame(self.window, bg="#303030")
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.timer_label = tk.Label(bottom_frame, text="0.00s", font=("Helvetica", 14), fg="#FFFFFF", bg="#303030")
        self.timer_label.pack(side=tk.RIGHT)
        
        self.play_button = ttk.Button(bottom_frame, text="Play", style="Play.TButton", command=self.toggle_algorithm).pack(side=tk.RIGHT, padx=10)

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_timer()

    def show_algorithm_info(self):
        # Crear una pequeña ventana emergente con la explicación del algoritmo
        info_window = tk.Toplevel(self.window)
        info_window.title("Explicación del Algoritmo")
        info_window.geometry("300x200")
        
        explanation = "Aquí va la explicación del algoritmo.\nPuede ser tan detallada como quieras."
        
        info_label = tk.Label(info_window, text=explanation, font=("Helvetica", 12), fg="#000000", padx=20, pady=20)
        info_label.pack()

        close_button = tk.Button(info_window, text="Cerrar", command=info_window.destroy)
        close_button.pack(pady=10)

    def validate_n(self, *args):
        if self.n.get() != "":
            try:
                value = int(self.n.get())
                if value < 1 or value > 250:
                    raise ValueError
            except ValueError:
                self.n.set("15")
            
    
    def toggle_algorithm(self):
        if self.n.get() != "":
            if self.is_running:
                self.is_running = False
            else:
                self.is_running = True
                self.start_time = time.time() - self.elapsed_time  # Continuar desde donde lo dejamos
            
            # Aquí podrías empezar o detener el algoritmo real de ordenamiento
            self.update_timer()
        else:
            self.item_count_entry.focus_force()
    
    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"{self.elapsed_time:.2f}s")
        self.window.after(100, self.update_timer)  # Actualiza el temporizador cada 100ms
        
    def create_theme(self):
        style = ttk.Style()
        if "myTheme" not in style.theme_names():
            style.theme_create("myTheme", parent="clam", settings={
                "Play.TButton": {
                    "configure": {"font": ("Helvetica", 12), "background": "#404040", "foreground": "#FFFFFF", "borderwidth": 0, "relief": "flat", "anchor": "center", "padding": (10, 5)},
                    "map": {"background": [("active", "#505050"), ("focus", "#505050")]}
                },
                "Title.TLabel": {
                    "configure": {"background": "#303030", "foreground": "#FFFFFF", "font": ("Helvetica", 16)}
                },
            })
