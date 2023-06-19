import curses

class ColorFrame:
    pass

def init_colors():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_WHITE)

    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_CYAN)

    curses.init_pair(100, curses.COLOR_WHITE, curses.COLOR_BLACK)

    colors = ColorFrame()

    colors.BLACK_WHITE = curses.color_pair(1)
    colors.YELLOW_WHITE = curses.color_pair(2)
    colors.BLUE_WHITE = curses.color_pair(3)
    colors.MAGENTA_WHITE = curses.color_pair(4)
    colors.RED_WHITE = curses.color_pair(5)
    colors.GREEN_WHITE = curses.color_pair(6)

    colors.WHITE_YELLOW = curses.color_pair(7)   
    colors.WHITE_BLUE = curses.color_pair(8)   
    colors.WHITE_MAGENTA = curses.color_pair(9)   
    colors.WHITE_RED = curses.color_pair(10)   
    colors.WHITE_GREEN = curses.color_pair(11)   
    colors.WHITE_CYAN = curses.color_pair(12)  

    colors.WHITE_BLACK = curses.color_pair(100)

    return colors