import config
import curses

from src.card import Minion
from src import draw
from time import sleep, time

class ColorFrame:
    pass

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_WHITE)

    colors = ColorFrame()
    colors.BLACK_TEXT = curses.color_pair(1)
    colors.GREEN_TEXT = curses.color_pair(4)
    colors.RED_TEXT = curses.color_pair(3)
    colors.WHITE_BACK = curses.color_pair(6)
    colors.BLUE_BACK = curses.color_pair(2)
    colors.GREEN_BACK = curses.color_pair(5)

    ###
    # TEMP STUFF
    ###
    test_card = Minion(2, 9, "Test_Card", 1, "Murloc")

    while True:
        s_time = time()

        scr.clear()

        key = scr.getch()
        if key == 27:
            break

        test_card.update(colors)
        test_card.draw(0, 0, scr, colors)

        scr.refresh()

        delay = max(0, config.FPS_RATIO - (time() - s_time))
        sleep(delay)

if __name__ == "__main__":
    curses.wrapper(main)