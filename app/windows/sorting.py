import tkinter as tk

class SortingWindow:
    def __init__(self, root, algorithm_name):
        self.window = tk.Toplevel(root)
        self.window.title(algorithm_name)
        self.window.geometry("600x400")
        self.window.configure(bg="black")

        label = tk.Label(self.window, text=f"Running {algorithm_name}...", fg="white", bg="black", font=("Arial", 16))
        label.pack(padx=20, pady=20)
