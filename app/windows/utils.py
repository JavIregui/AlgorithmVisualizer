def calculate_window_position(root, win_width, win_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    root.update_idletasks()
    menu_x = root.winfo_x()
    menu_y = root.winfo_y()
    menu_width = root.winfo_width()
    menu_height = root.winfo_height()
    
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

    return win_x, win_y