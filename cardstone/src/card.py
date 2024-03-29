import config
import copy
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
    def __init__(self, name:str, mana: str, faction:str):
        self.name = name
        self.default_mana = mana
        self.cur_mana = mana
        self.faction = faction

        self.selected = False
        self.select_speed = 2
        self.select_tracker = 0

        self.usable = False
        self.usable_bonus = False
        self.u_y = 0
        self.u_x = 0
        self.section = 0


    def set_selected(self, val:bool):
        self.selected = val

    def set_usable(self, val:bool):
        self.usable = val

        if not val:
            self.usable_bonus = val

    def set_usable_bonus(self, val:bool):
        self.usable = val
        self.usable_bonus = val

    def get_generator(self):
        while True:
            yield copy.deepcopy(self)
        
    def draw(self, y:int, x:int, scr, colors):
        draw.rectangle(y + config.OUTLINE_OFFSET_Y, x + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, scr, colors.GREY_BACK)

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

        do_mana, mana_c = stat_color_change(self.cur_mana, self.default_mana, colors, inverted=True)
        if do_mana:
            mana_s = str(self.cur_mana)
            mana_y = y + config.MANA_OFFSET_Y
            mana_x = x + 1

            scr.addstr(mana_y + config.OUTLINE_OFFSET_Y, mana_x + config.OUTLINE_OFFSET_X, mana_s, mana_c)

        if self.faction is not None:
            faction_ss = f"-{self.faction}-"
            faction_s = f"{faction_ss:^{config.CARD_WIDTH}}"
            faction_y = y + config.FACTION_OFFSET_Y

            scr.addstr(faction_y + config.OUTLINE_OFFSET_Y, x + config.OUTLINE_OFFSET_X, faction_s, colors.GREY_BACK)
            

        if self.selected:
            self.select_tracker = (self.select_tracker + 1) % 1000000

            if self.select_tracker & self.select_speed:
                tb_s = " " * (config.CARD_WIDTH + 2)
                bot_y = y + config.CARD_HEIGHT + 1

                scr.addstr(y, x, tb_s, colors.GREEN_BACK)
                scr.addstr(bot_y, x, tb_s, colors.GREEN_BACK)

                for yy in range(config.CARD_HEIGHT):
                    lr_y = y + yy + 1
                    right_x = x + config.CARD_WIDTH + 1

                    scr.addstr(lr_y, x, " ", colors.GREEN_BACK)
                    scr.addstr(lr_y, right_x, " ", colors.GREEN_BACK)
        elif self.usable:
            if self.section == 0:
                self.u_x = self.u_x + 1

                if self.u_x > config.CARD_WIDTH:
                    self.section = 1
            elif self.section == 1:
                self.u_y += 1

                if self.u_y > config.CARD_HEIGHT:
                    self.section = 2
            elif self.section == 2:
                self.u_x = self.u_x - 1

                if self.u_x == 0:
                    self.section = 3
            elif self.section == 3:
                self.u_y -= 1

                if self.u_y == 0:
                    self.section = 0

            if self.usable_bonus:
                local_color = colors.YELLOW_BACK
            else:
                local_color = colors.GREEN_BACK

            scr.addstr(y + self.u_y, x + self.u_x, " ", local_color)

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

class Deck(Card):
    def __init__(self):
        super().__init__("", 0, None)

    def draw(self, y:int, x:int, scr, colors, deck_len):
        super().draw(y, x, scr, colors)

        draw.rectangle(y + config.OUTLINE_OFFSET_Y, x + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, scr, colors.WHITE_BACK)

        deck_ss = f"Deck: ({deck_len})"
        deck_s = f"{deck_ss:^{config.CARD_WIDTH}}"
        faction_y = y + config.DECK_OFFSET_Y

        scr.addstr(faction_y + config.OUTLINE_OFFSET_Y, x + config.OUTLINE_OFFSET_X, deck_s, colors.WHITE_BACK)

# Minions
m_One_gen = Minion(1, 1, "One", 1, None).get_generator()
m_Two_gen = Minion(2, 2, "Two", 2, None).get_generator()
m_Three_gen = Minion(3, 3, "Three", 3, None).get_generator()
m_Four_gen = Minion(4, 4, "Four", 4, None).get_generator()
m_Five_gen = Minion(5, 5, "Five", 5, None).get_generator()