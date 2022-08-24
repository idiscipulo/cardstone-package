def rectangle(y:int, x:int, w:int, h:int, scr, color):
    for hh in range(h):
        scr.addstr(y + hh, x, f"{' ':{w}}", color)