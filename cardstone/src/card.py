import config
import curses
import math

from src import draw

def stat_color_change(t_cur:int, t_max:int, colors, inverted:bool=False):
    ret_b = False
    ret_c = 0
    c_list = [colors.RED_TEXT, colors.GREEN_TEXT]

    if t_cur < t_max:
        ret_b = True
        ret_c = 0
    elif t_cur > t_max:
        ret_b = True
        ret_c = 1

    if inverted:
        ret_c = (ret_c + 1) % 2

    return ret_b, c_list[ret_c]

class Card:
    def __init__(self, name:str, mana:int, faction:str):
        self.name = name
        self.max_mana = mana
        self.cur_mana = mana
        self.faction = faction

        self.usable = False
        self.selected = True

        self.flash = False
        self.flash_speed = 2
        self.flash_tracker = 0
        self.flash_color = None
    
    def update(self, colors):
        if self.usable:
            self.flash = True
            self.flash_color = colors.GREEN_BACK
        elif self.selected:
            self.flash = True
            self.flash_color = colors.WHITE_BACK
        else:
            self.flash = False
        
    def draw(self, y:int, x:int, scr, colors):
        draw.rectangle(y + config.OUTLINE_OFFSET_Y, x + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, scr, colors.BLUE_BACK)

        text_y = y + config.TEXT_OFFSET_Y
        text_x = x + config.TEXT_OFFSET_X
        draw.rectangle(text_y + config.OUTLINE_OFFSET_Y, text_x + config.OUTLINE_OFFSET_X, config.TEXT_WIDTH, config.TEXT_HEIGHT, scr, colors.BLACK_TEXT)

        title_s = f"{self.name:^{config.TITLE_WIDTH}}"
        title_y = y
        title_x = x

        mana_s = f"({self.cur_mana})"
        mana_y = y + config.MANA_OFFSET_Y
        mana_x = x

        scr.addstr(title_y + config.OUTLINE_OFFSET_Y, title_x + config.OUTLINE_OFFSET_X, title_s, colors.BLACK_TEXT)
        scr.addstr(mana_y + config.OUTLINE_OFFSET_Y, mana_x + config.OUTLINE_OFFSET_X, mana_s, colors.BLACK_TEXT)

        do_mana, mana_c = stat_color_change(self.cur_mana, self.max_mana, colors, inverted=True)
        if do_mana:
            mana_s = str(self.cur_mana)
            mana_y = y + config.MANA_OFFSET_Y
            mana_x = x + 1

            scr.addstr(mana_y + config.OUTLINE_OFFSET_Y, mana_x + config.OUTLINE_OFFSET_X, mana_s, mana_c)

        if self.flash:
            self.flash_tracker = (self.flash_tracker + 1) % 1000000

            if self.flash_tracker & self.flash_speed:
                tb_s = " " * (config.CARD_WIDTH + 2)
                bot_y = config.CARD_HEIGHT + 1

                scr.addstr(y, x, tb_s, self.flash_color)
                scr.addstr(y + bot_y, x, tb_s, self.flash_color)

                for yy in range(config.CARD_HEIGHT):
                    lr_y = yy + 1
                    right_x = x + config.CARD_WIDTH + 1

                    scr.addstr(lr_y, x, " ", self.flash_color)
                    scr.addstr(lr_y, right_x, " ", self.flash_color)


class Minion(Card):
    def __init__(self, attack:int, health:int, *args):
        super().__init__(*args)

        self.max_attack = attack
        self.cur_attack = attack
        self.max_health = health
        self.cur_health = health

    def draw(self, y:int, x:int, scr, colors):
        super().draw(y, x, scr, colors)

        stat_s = f"[{self.cur_attack}/{self.cur_health}]"
        stat_y = y + config.STAT_OFFSET_Y
        stat_offset_x = config.CARD_WIDTH - len(stat_s)
        stat_x = x + stat_offset_x

        scr.addstr(stat_y + config.OUTLINE_OFFSET_Y, stat_x + config.OUTLINE_OFFSET_X, stat_s, colors.BLACK_TEXT)

        do_attack, attack_c = stat_color_change(self.cur_attack, self.max_attack, colors)
        if do_attack:
            attack_s = str(self.cur_attack)
            attack_y = y + config.STAT_OFFSET_Y
            attack_offset_x = config.CARD_WIDTH + 1 - len(stat_s)
            attack_x = x + attack_offset_x

            scr.addstr(attack_y + config.OUTLINE_OFFSET_Y, attack_x + config.OUTLINE_OFFSET_X, attack_s, attack_c)

        do_health, health_c = stat_color_change(self.cur_health, self.max_health, colors)
        if do_health:
            health_s = str(self.cur_health)
            health_y = y + config.STAT_OFFSET_Y
            health_offset_x = config.CARD_WIDTH - len(f"{self.cur_health}]")
            health_x = x + health_offset_x

            scr.addstr(health_y + config.OUTLINE_OFFSET_Y, health_x + config.OUTLINE_OFFSET_X, health_s, health_c)
