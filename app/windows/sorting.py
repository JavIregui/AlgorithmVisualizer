import tkinter as tk
from .utils import calculate_window_position

class SortingWindow:
    def __init__(self, root, algorithm_name, offset):
        
        self.window = tk.Toplevel(root)
        self.window.title(algorithm_name)
        
        self.window.configure(bg="#303030")
        
        win_width = 600
        win_height = 400
        
        win_x, win_y = calculate_window_position(root, win_width, win_height, offset)

        self.window.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

        label = tk.Label(self.window, text=f"Running {algorithm_name}...", 
                        font=("Helvetica", 16), fg="#FFFFFF", bg="#303030")
        label.pack(padx=25 ,pady=20)
        
