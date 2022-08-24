import config
import curses
import os

from src.card import Minion
from src import draw
from time import sleep, time

class ColorFrame:
    pass

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_WHITE)

    colors = ColorFrame()
    colors.BLACK_TEXT = curses.color_pair(1)
    colors.GREEN_TEXT = curses.color_pair(4)
    colors.RED_TEXT = curses.color_pair(3)
    colors.WHITE_TEXT = curses.color_pair(2)
    colors.WHITE_BACK = curses.color_pair(6)
    colors.GREY_BACK = curses.color_pair(1) | curses.A_STANDOUT # black text, white background, standout -> grey background
    colors.GREEN_BACK = curses.color_pair(5)

    ###
    # TEMP STUFF
    ###
    card_1 = Minion(2, 9, "Practice Dummy", 10, "Murloc")
    card_2 = Minion(2, 9, "Practice Dummy", 10, "Murloc")
    card_3 = Minion(2, 9, "Practice Dummy", 10, "Murloc")
    card_4 = Minion(2, 9, "Practice Dummy", 10, "Murloc")
    card_5 = Minion(2, 9, "Practice Dummy", 10, "Murloc")

    while True:
        s_time = time()

        scr.clear()

        key = scr.getch()
        if key == 27:
            break

        card_1.draw(0, 0, scr, colors)
        card_2.draw(0, config.CARD_SPACE * 1, scr, colors)
        card_3.draw(0, config.CARD_SPACE * 2, scr, colors)
        card_4.draw(0, config.CARD_SPACE * 3, scr, colors)
        card_5.draw(0, config.CARD_SPACE * 4, scr, colors)

        scr.refresh()

        delay = max(0, config.FPS_RATIO - (time() - s_time))
        sleep(delay)

if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    og_width = terminal_size.columns
    og_height = terminal_size.lines
    os.system(f'mode con: cols={config.WIDTH} lines={config.HEIGHT}')

    curses.wrapper(main)

    os.system(f'mode con: cols={og_width} lines={og_height}')
