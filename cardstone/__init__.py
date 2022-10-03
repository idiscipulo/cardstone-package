import config
import curses
import os

from src import draw
from src.game import Game
from time import sleep, time

class ColorFrame:
    pass

def comp_actual_fps(s_time):
    actual_time = max(0.00001, time() - s_time)
    actual_fps = 1 / actual_time

    return int(actual_fps)

def init_colors():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    colors = ColorFrame()
    colors.BLACK_TEXT = curses.color_pair(1)
    colors.WHITE_BACK = curses.color_pair(1)

    colors.WHITE_TEXT = curses.color_pair(2)
    colors.BLACK_BACK = curses.color_pair(2)

    colors.RED_TEXT = curses.color_pair(3)
    colors.GREEN_TEXT = curses.color_pair(4)

    colors.GREEN_BACK = curses.color_pair(5)
    colors.YELLOW_BACK = curses.color_pair(6)

    colors.GREY_BACK = curses.color_pair(1) | curses.A_STANDOUT # black text, white background, standout -> grey background


    return colors

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    colors = init_colors()

    scr.bkgd(colors.BLACK_BACK) # set a white background

    game = Game(scr, colors)
    
    anim_time = time()

    while True:
        s_time = time()

        # inputs
        key = scr.getch()
        if key == 9: # tab
            config.SHOW_DEV_STATS = not config.SHOW_DEV_STATS
        elif key == 27: # escape
            break

        if key != -1:
            k = key

        # update at the FPS (60)
        game.update(key)

        # draw at the animation FPS (12)
        if s_time - anim_time > config.ANIM_FPS_RATIO:
            scr.clear()

            game.draw(colors)

            scr.refresh()

            anim_time = s_time
        
        delay = max(0, config.FPS_RATIO - (time() - s_time))

        sleep(delay)

        if config.SHOW_DEV_STATS:
            actual_fps = comp_actual_fps(s_time)
            scr.addstr(0, 0, f"= Developer Stats =")
            scr.addstr(1, 0, f"fps:      {actual_fps}")
            scr.addstr(2, 0, f"last_key: {k}")

if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    og_width = terminal_size.columns
    og_height = terminal_size.lines
    os.system(f'mode con: cols={config.WIDTH} lines={config.HEIGHT}')

    curses.wrapper(main)

    os.system(f'mode con: cols={og_width} lines={og_height}')
