from algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
)

import random

ALGORORITHMS_CONFIG = {
    "Bubble Sort": {
        "function": bubble_sort,
        "description": "Bubble Sort is a simple sorting algorithm that repeatedly compares and swaps adjacent elements until the list is sorted. It has an O(n²) time complexity, making it inefficient for large lists."
    },
    "Selection Sort": {
        "function": selection_sort,
        "description": "Selection Sort is a sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element. It has an O(n²) time complexity."
    },
    "Insertion Sort": {
        "function": insertion_sort,
        "description": "Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time by repeatedly inserting the next unsorted element into its correct position within the sorted part of the list. It has an O(n²) time complexity, making it inefficient for large datasets."
    },
    "Quick Sort": {
        "function": quick_sort,
        "description": "Quick Sort is a divide-and-conquer sorting algorithm that selects a pivot, partitions the list into elements smaller and greater than the pivot, and recursively sorts both parts. It has an average time complexity of O(n log n), making it efficient for large lists."
    },
}

def generate_data(n):
    data = list(range(1, n + 1))
    random.shuffle(data)
    return data      

def draw(canvas, data, selected, done):
    canvas.delete("all")
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    if not data or canvas_width <= 0 or canvas_height <= 0:
        return
    
    num_bars = len(data)
    bar_width = canvas_width / num_bars
    
    max_val = max(data)
    min_val = min(data)
    
    for i, value in enumerate(data):
        if max_val == min_val:
            bar_height = canvas_height
        else:
            bar_height = (canvas_height / max_val) * value
        
        x0 = i * bar_width
        y0 = canvas_height - bar_height
        x1 = x0 + bar_width
        y1 = canvas_height
        
        if i in selected:
            color = "#FF0000"
        else:
            color = "#FFFFFF"
            
        if done:
            color = "#00FF00"
        
        canvas.create_rectangle(
            x0, y0, x1, y1,
            fill=color,
            outline="#303030",
            width=1
        ) 

def calculate_window_position(root, win_width, win_height, offset):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    root.update_idletasks()
    menu_x = root.winfo_x()
    menu_y = root.winfo_y()
    menu_width = root.winfo_width()
    menu_height = root.winfo_height()
    
    if menu_x + menu_width + win_width + 5 * offset <= screen_width:
        win_x = menu_x + menu_width + 5 * offset
        win_y = menu_y
    elif menu_x - win_width - 5 * offset >= 0:
        win_x = menu_x - win_width - 5 * offset
        win_y = menu_y
    else:
        if menu_y + menu_height + win_height + 5 * offset <= screen_height:
            win_x = menu_x
            win_y = menu_y + menu_height + 5 * offset
        elif menu_y - win_height - 5 * offset >= 0:
            win_x = menu_x
            win_y = menu_y - win_height - 5 * offset
        else:
            win_x = (screen_width - win_width) // 2 + 5 * offset
            win_y = (screen_height - win_height) // 2 + 5 * offset

    return win_x, win_y