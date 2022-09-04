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
        - MULLIGAN_START        -- <animation> draw starting hand, [text] "Start Game"
        - MULLIGAN_SELECT       -- (choice) select cards to redraw, [text] "Choose cards to redraw"
        - MULLIGAN_REDRAW       -- <animation> swapping cards, <animation> lower cards from middle to back row, [text] "Player X, Your Turn"
        - PLAYER_START          -- <animation> draw card
        - PLAYER_TURN           -- (choice) select cards to play or attack with
        - CARD_EFFECTS          -- <animation> show card effects
        - ENEMY_START           -- <animation> draw card, [text] "Enemy X, Your Turn"
        - ENEMY_TURN            -- {process} waiting for AI / opposing player input
        - PLAYER_WIN            -- <animation> you win animation
        - ENEMY_WIN             -- <animation> you lose animation
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

        dt_y = config.PLAYER_BACK_Y
        dt_x = config.DECK_X
        dt_ss = f"DECK [{len(self.player.deck)}]"
        dt_s = f"{dt_ss:^{config.CARD_WIDTH}}"

        self.scr.addstr(dt_y, dt_x + config.OUTLINE_OFFSET_X, dt_s, colors.WHITE_TEXT)

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

        dt_y = config.ENEMY_BACK_Y
        dt_x = config.DECK_X
        dt_ss = f"DECK [{len(self.player.deck)}]"
        dt_s = f"{dt_ss:^{config.CARD_WIDTH}}"

        self.scr.addstr(dt_y, dt_x + config.OUTLINE_OFFSET_X, dt_s, colors.WHITE_TEXT)