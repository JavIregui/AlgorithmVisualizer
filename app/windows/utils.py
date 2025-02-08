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