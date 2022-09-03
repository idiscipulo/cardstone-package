import config

from src import draw
from src import player

DOWN = 258
UP = 259
LEFT = 260
RIGHT = 261
ENTER = 10

class Game:
    """

    states:
        - 
    """

    def __init__(self, scr, colors):
        self.scr = scr

        self.player = player.Player(colors)
        self.enemy = player.Player(colors)

        self.player.shuffle_deck()
        self.player.draw_starting_hand()

        self.enemy.shuffle_deck()
        self.enemy.draw_starting_hand()

        self.player.fill_board()
        self.enemy.fill_board()

    def draw_mana(y:int, x:int, cur_mana:int, max_mana:int):
        draw.rectangle(y + config.MANA_BAR_OFFSET_Y, x + config.MANA_BAR_OFFSET_X, config.MANA_BAR_WIDHT, config.MANA_BAR_HEIGHT, self.scr, colors.GREY_BACK)
    
    def update(self, key:int):
        pass

    def draw(self, colors):

        # center
        c_str = "■—" * int(config.WIDTH / 2)

        self.scr.addstr(22, 0, c_str, colors.WHITE_TEXT)

        ##########
        # PLAYER #
        ##########

        # hand
        for dx, card in enumerate(self.player.hand):
            hand_space_center = (config.CARD_SPACE * 5) / 2
            hand_width_center = (config.CARD_SPACE * len(self.player.hand)) / 2
            center_offset_x = int(hand_space_center - hand_width_center)

            card.draw(config.PLAYER_BACK_Y, (dx * config.CARD_SPACE) + config.CARD_SPACE_PADDING + center_offset_x, self.scr, colors)

        # board
        for dx, card in enumerate(self.player.board):
            board_space_center = (config.CARD_SPACE * 5) / 2
            board_width_center = (config.CARD_SPACE * len(self.player.board)) / 2
            center_offset_x = int(board_space_center - board_width_center)

            card.draw(config.PLAYER_FRONT_Y, (dx * config.CARD_SPACE) + config.CARD_SPACE_PADDING + center_offset_x, self.scr, colors)

        # deck
        dy = config.PLAYER_BACK_Y
        dx = config.DECK_X

        draw.rectangle(dy + config.OUTLINE_OFFSET_Y, dx + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, self.scr, self.player.card_back)

        if self.player.card_back in [colors.WHITE_BACK]:
            deck_text_color = colors.WHITE_TEXT
        else:
            deck_text_color = colors.BLACK_TEXT

        dt_y = config.PLAYER_DECK_TEXT_Y
        dt_x = config.DECK_TEXT_X
        dt_ss = "DECK"
        dt_s = f"{dt_ss:^{config.DECK_TEXT_WIDTH}}"

        self.scr.addstr(dt_y + config.OUTLINE_OFFSET_Y, dt_x + config.OUTLINE_OFFSET_X, dt_s, deck_text_color)

        dtc_y = config.PLAYER_DECK_COUNT_Y
        dtc_x = config.DECK_COUNT_X
        dtc_ss = f"{len(self.player.deck)}"
        dtc_s = f"{dtc_ss:^{config.DECK_COUNT_WIDTH}}"

        self.scr.addstr(dtc_y + config.OUTLINE_OFFSET_Y, dtc_x + config.OUTLINE_OFFSET_X, dtc_s, deck_text_color)

        ##########
        # ENEMY #
        ##########

        # hand
        for dx, card in enumerate(self.enemy.hand):
            hand_space_center = (config.CARD_SPACE * 5) / 2
            hand_width_center = (config.CARD_SPACE * len(self.enemy.hand)) / 2
            center_offset_x = int(hand_space_center - hand_width_center)

            card.draw(config.ENEMY_BACK_Y, (dx * config.CARD_SPACE) + config.CARD_SPACE_PADDING + center_offset_x, self.scr, colors)

        # board
        for dx, card in enumerate(self.enemy.board):
            board_space_center = (config.CARD_SPACE * 5) / 2
            board_width_center = (config.CARD_SPACE * len(self.enemy.board)) / 2
            center_offset_x = int(board_space_center - board_width_center)

            card.draw(config.ENEMY_FRONT_Y, (dx * config.CARD_SPACE) + config.CARD_SPACE_PADDING + center_offset_x, self.scr, colors)

        # deck
        dy = config.ENEMY_BACK_Y
        dx = config.DECK_X

        draw.rectangle(dy + config.OUTLINE_OFFSET_Y, dx + config.OUTLINE_OFFSET_X, config.CARD_WIDTH, config.CARD_HEIGHT, self.scr, self.enemy.card_back)

        if self.enemy.card_back in [colors.WHITE_BACK]:
            deck_text_color = colors.WHITE_TEXT
        else:
            deck_text_color = colors.BLACK_TEXT

        dt_y = config.ENEMY_DECK_TEXT_Y
        dt_x = config.DECK_TEXT_X
        dt_ss = "DECK"
        dt_s = f"{dt_ss:^{config.DECK_TEXT_WIDTH}}"

        self.scr.addstr(dt_y + config.OUTLINE_OFFSET_Y, dt_x + config.OUTLINE_OFFSET_X, dt_s, deck_text_color)

        dtc_y = config.ENEMY_DECK_COUNT_Y
        dtc_x = config.DECK_COUNT_X
        dtc_ss = f"{len(self.enemy.deck)}"
        dtc_s = f"{dtc_ss:^{config.DECK_COUNT_WIDTH}}"

        self.scr.addstr(dtc_y + config.OUTLINE_OFFSET_Y, dtc_x + config.OUTLINE_OFFSET_X, dtc_s, deck_text_color)