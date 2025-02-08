import tkinter as tk

class SearchWindow:
    def __init__(self, root, algorithm_name):
        
        self.window = tk.Toplevel(root)
        self.window.title(algorithm_name)
        
        self.window.configure(bg="#303030")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.update_idletasks()
        menu_x = self.root.winfo_x()
        menu_y = self.root.winfo_y()
        menu_width = self.root.winfo_width()
        menu_height = self.root.winfo_height()
        
        win_width, win_height = 600, 400
        
        if menu_x + menu_width + win_width + 5 <= screen_width:
            win_x = menu_x + menu_width + 5
            win_y = menu_y
        elif menu_x - win_width - 5 >= 0:
            win_x = menu_x - win_width - 5
            win_y = menu_y
        else:
            if menu_y + menu_height + win_height + 5 <= screen_height:
                win_x = menu_x
                win_y = menu_y + menu_height + 5
            elif menu_y - win_height - 5 >= 0:
                win_x = menu_x
                win_y = menu_y - win_height - 5
            else:
                win_x = (screen_width - win_width) // 2
                win_y = (screen_height - win_height) // 2

        self.algorithm_window.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

        label = tk.Label(self.algorithm_window, text=f"Running {self.selected_algorithm}...", 
                        font=("Helvetica", 16), fg="#FFFFFF", bg="#303030")
        label.pack(padx=25 ,pady=20)
