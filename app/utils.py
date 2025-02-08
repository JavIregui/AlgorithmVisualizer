from .windows.sorting import SortingWindow
from .windows.search import SearchWindow

ALGORITHMS = {
    "Bubble Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Selection Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Insertion Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Merge Sort":   {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Quick Sort":   {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Heap Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Radix Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Counting Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Shell Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Cocktail Shaker Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Tim Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    "Gnome Sort":  {"type": "Sorting algorithms", "window_class": SortingWindow},
    
    "Linear Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Binary Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Jump Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Exponential Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Interpolation Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Ternary Search": {"type": "Search algorithms", "window_class": SearchWindow},
    "Fibonacci Search": {"type": "Search algorithms", "window_class": SearchWindow},
    
    "Dijkstra": {"type": "Graph algorithms", "window_class": SearchWindow},
    "A*": {"type": "Graph algorithms", "window_class": SearchWindow},
    "Breadth-First Search (BFS)": {"type": "Graph algorithms", "window_class": SearchWindow},
    "Depth-First Search (DFS)": {"type": "Graph algorithms", "window_class": SearchWindow},
    
    "N Queen Problem": {"type": "Backtracking algorithms", "window_class": SearchWindow},
    "Sudoku Solver": {"type": "Backtracking algorithms", "window_class": SearchWindow},
    "Knight's Tour": {"type": "Backtracking algorithms", "window_class": SearchWindow},
    
    "Recursive Backtracking": {"type": "Maze generation algorithms", "window_class": SearchWindow},
    "Prim's Algorithm": {"type": "Maze generation algorithms", "window_class": SearchWindow},
    "Kruskal's Algorithm": {"type": "Maze generation algorithms", "window_class": SearchWindow},
    
    "Genetic Algorithm": {"type": "Evolutionary algorithms", "window_class": SearchWindow},
    
    "Convex Hull (Graham's Algorithm)": {"type": "Geometric algorithms", "window_class": SearchWindow},
}