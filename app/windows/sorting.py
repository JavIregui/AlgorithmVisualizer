import tkinter as tk
from tkinter import ttk
import time

from .utils import ALGORORITHMS_CONFIG, generate_data, draw, calculate_window_position

class SortingWindow:
    def __init__(self, root, algorithm_name, offset):
        
        self.algorithm_name = algorithm_name
        self.algorithm_config = ALGORORITHMS_CONFIG[algorithm_name]
        
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
        
        # Grid configuration
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Top Frame
        self.top_frame = tk.Frame(self.window, bg="#303030")
        self.top_frame.grid(row=0, column=0, padx=25, pady=20, sticky="ew")
        
        # Label
        ttk.Label(self.top_frame, text=algorithm_name, style="Title.TLabel").pack(side=tk.LEFT)
        
        # Learn more button
        ttk.Button(self.top_frame, text="Learn more", style="Play.TButton", command=self.show_algorithm_info).pack(side=tk.LEFT, padx=20)
        self.description_open = False
        
        # Item counter
        self.n = tk.StringVar(value="100")
        self.n.trace_add("write", self.validate_n)
        
        self.item_count_entry = tk.Entry(self.top_frame, font=("Helvetica", 12), justify="center", insertbackground="#FFFFFF", borderwidth=0, border=0, highlightthickness=0, bg="#404040", fg="#FFFFFF", relief="flat", width=5, textvariable=self.n)
        self.item_count_entry.pack(side=tk.RIGHT)
        tk.Label(self.top_frame, text="n:", font=("Helvetica", 12), fg="#FFFFFF", bg="#303030").pack(side=tk.RIGHT, padx=5)
        
        # Canvas
        self.data = generate_data(int(self.n.get()))
        self.canvas = tk.Canvas(self.window, bg="#404040", highlightthickness=0, border=0, borderwidth=0, relief="flat")
        self.canvas.grid(row=1, column=0, padx=25, sticky="nsew")
        self.window.update_idletasks()
        draw(self.canvas, self.data, [], False)
         
        # Bottom frame
        bottom_frame = tk.Frame(self.window, bg="#303030")
        bottom_frame.grid(row=2, column=0, padx=25, pady=20, sticky="ew")
        
        # Reset button
        self.reset_button = ttk.Button(bottom_frame, text="Reset", style="Play.TButton", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Timer
        self.timer_label = tk.Label(bottom_frame, text="0.000s", font=("Helvetica", 14), fg="#FFFFFF", bg="#303030")
        self.timer_label.pack(side=tk.RIGHT)
        
        # Play button
        self.play_button = ttk.Button(bottom_frame, text="Play", style="Play.TButton", command=self.toggle_algorithm)
        self.play_button.pack(side=tk.RIGHT, padx=10)

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_timer()
        
        self.reset()
        
    def execute_algorithm(self):
        algorithm_function = self.algorithm_config["function"]
        result = algorithm_function(self.data)
        self.toggle_algorithm()

    def show_algorithm_info(self):
        if not self.description_open:
            self.description_open = True
            info_window = tk.Toplevel(self.window)
            info_window.title("Learn more")
            info_window.configure(bg="#303030")
            
            explanation = self.algorithm_config["description"]
            
            info_label = tk.Label(info_window, text=explanation, font=("Helvetica", 10),
                                bg="#303030", fg="#FFFFFF", padx=10, pady=10, 
                                wraplength=350, anchor="w", justify="left")
            info_label.pack()

            info_window.update_idletasks()
            content_height = info_label.winfo_reqheight() + 25
            
            window_height = min(content_height, 300)
            
            x_pos = self.win_x + self.win_width // 2 - 200
            y_pos = self.win_y + self.win_height // 2 - (window_height // 2)
            
            info_window.geometry(f"400x{window_height}+{x_pos}+{y_pos}")
            info_window.resizable(False, False)
            
            info_window.protocol("WM_DELETE_WINDOW", lambda: self.close_info_window(info_window))

    def close_info_window(self, window):
        self.description_open = False
        window.destroy()
    
    def validate_n(self, *args):
        if self.n.get() != "":
            try:
                value = int(self.n.get())
                if value < 1 or value > 250:
                    raise ValueError
            except ValueError:
                self.n.set("100")
                
            self.reset()
    
    def toggle_algorithm(self):
        if self.n.get() != "":
            if self.is_running:
                self.play_button.config(text="Play")
                self.is_running = False
            else:
                self.play_button.config(text="Stop")
                self.is_running = True
                self.start_time = time.time() - self.elapsed_time
                self.execute_algorithm()
            
            self.update_timer()
        else:
            self.item_count_entry.focus_force()
    
    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"{self.elapsed_time:.3f}s")
        self.window.after(10, self.update_timer)
        
    def reset(self):
        self.is_running = False
        self.play_button.config(text="Play")
        
        self.elapsed_time = 0
        self.timer_label.config(text=f"{self.elapsed_time:.3f}s")
        
        self.data = generate_data(int(self.n.get()))
        self.window.update_idletasks()
        draw(self.canvas, self.data, [], False)
        
        self.update_timer()
         
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
