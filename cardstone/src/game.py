import random

import config
from src import card
from src import draw

class Player:
    def __init__(self):
        self.deck = [
            card.MINION_one
            , card.MINION_two
            , card.MINION_three
            , card.MINION_four
            , card.MINION_five
            , card.MINION_one
            , card.MINION_two
            , card.MINION_three
            , card.MINION_four
            , card.MINION_five
            , card.MINION_one
            , card.MINION_two
            , card.MINION_three
            , card.MINION_four
            , card.MINION_five
        ]

        self.hand = []
        self.graveyard = []
        
        self.cur_mana = 0
        self.max_mana = 0

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def shuffle_graveyard(self):
        random.shuffle(self.graveyard)

    def draw_card(self):
        if len(self.hand) < 5:
            top = self.deck.pop(0)
            self.hand.append(top)

    def draw_starting_hand(self):
        for i in range(5):
            self.draw_card()

class Game:
    def __init__(self, scr, colors):
        self.scr = scr
        self.colors = colors

        self.player = Player()
        self.enemy = Player()

        self.player.shuffle_deck()
        self.player.draw_starting_hand()

        self.enemy.shuffle_deck()
        self.enemy.draw_starting_hand()

    def draw_mana(y:int, x:int, cur_mana:int, max_mana:int):
        draw.rectangle(y + config.MANA_BAR_OFFSET_Y, x + config.MANA_BAR_OFFSET_X, config.MANA_BAR_WIDHT, config.MANA_BAR_HEIGHT, self.scr, self.colors.GREY_BACK)
    
    def draw(self):
        draw.rectangle(18, 0, config.WIDTH, 1, self.scr, self.colors.WHITE_BACK)

        for dx, card in enumerate(self.player.hand):
            hand_space_center = (config.CARD_SPACE * 5) / 2
            hand_width_center = (config.CARD_SPACE * len(self.player.hand)) / 2
            center_offset_x = int(hand_space_center - hand_width_center)

            card.draw(config.PLAYER_BOTTOM_Y, (dx * config.CARD_SPACE) + config.CARD_SPACE_PADDING_X + center_offset_x, self.scr, self.colors)

        dy = config.PLAYER_BOTTOM_Y
        dx = config.DECK_X

        draw.rectangle(dy, dx, config.CARD_WIDTH + 2, config.CARD_HEIGHT + 2, self.scr, self.colors.WHITE_BACK)
        draw.rectangle(dy + config.OUTLINE_OFFSET_Y, dx + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, self.scr, self.colors.GREY_BACK)

        dt_y = config.PLAYER_BOTTOM_Y + config.PLAYER_DECK_TEXT_OFFSET_Y
        dt_x = config.DECK_X + config.DECK_TEXT_OFFSET_X
        dt_ss = "DECK"
        dt_s = f"{dt_ss:^{config.DECK_TEXT_WIDTH}}"

        self.scr.addstr(dt_y + config.OUTLINE_OFFSET_Y, dt_x + config.OUTLINE_OFFSET_X, dt_s, self.colors.BLACK_TEXT)

        dtc_y = config.PLAYER_BOTTOM_Y + config.PLAYER_DECK_COUNT_OFFSET_Y
        dtc_x = config.DECK_X + config.DECK_COUNT_OFFSET_X
        dtc_ss = f"{len(self.player.deck)}"
        dtc_s = f"{dtc_ss:^{config.DECK_COUNT_WIDTH}}"

        self.scr.addstr(dtc_y + config.OUTLINE_OFFSET_Y, dtc_x + config.OUTLINE_OFFSET_X, dtc_s, self.colors.BLACK_TEXT)