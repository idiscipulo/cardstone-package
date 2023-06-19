import curses
import os
from time import sleep, time

import configs
from card import Card
from colors import init_colors

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    colors = init_colors()

    scr.bkgd(colors.WHITE_BLACK) # set a gray background
    
    anim_time = time()

    show_dev_stats = False

    while True:
        s_time = time()

        # inputs
        key = scr.getch()
        if key == 9: # tab
            show_dev_stats = not show_dev_stats
        elif key == 27: # escape
            break

        if key != -1:
            k = key

        # update at the FPS (60)
        # game.update(key)

        # draw at the animation FPS (12)
        if s_time - anim_time > configs.ANIM_FPS_RATIO:
            scr.clear()

            Card(
                name    = "Rainbow Beast"
                , cost  = "YYR"
                , desc  = "Flying{br}{T}: Deal 1 damage to any target."
                , tags   = ["MINION"]
                , power = "4"
                , toughness = "4"
            ).draw(1, 1, scr, colors)

            scr.refresh()

            anim_time = s_time
        
        delay = max(0, configs.FPS_RATIO - (time() - s_time))

        sleep(delay)

        if show_dev_stats:
            actual_fps = comp_actual_fps(s_time)
            scr.addstr(0, 0, f"= Developer Stats =")
            scr.addstr(1, 0, f"fps:      {actual_fps}")
            scr.addstr(2, 0, f"last_key: {k}")

if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    og_width = terminal_size.columns
    og_height = terminal_size.lines
    os.system(f'mode con: cols={configs.WIDTH} lines={configs.HEIGHT}')

    curses.wrapper(main)

    os.system(f'mode con: cols={og_width} lines={og_height}')