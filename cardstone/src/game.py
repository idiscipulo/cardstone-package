import config

from src import draw
from src import player

DOWN = 258
UP = 259
LEFT = 260
RIGHT = 261
ENTER = 10

DEBUG = ""

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

        self.state_str = "PLAYER TURN"

        self.can_select = True
        self.select_y = 0
        self.select_x = 0
        self.rows = [
            self.enemy.hand
            , self.enemy.board
            , self.player.board
            , self.player.hand
        ]

        # start selected at the player icon (only thing guaranteed to exist always)
        self.select_y = 2
        self.select_x = len(self.player.board) - 1

        # for minion in self.enemy.board:
        #     minion.set_usable_bonus(True)

    def update(self, key:int):
        change = False

        if self.can_select:
            cur_row = self.rows[self.select_y]
            cur_obj = cur_row[self.select_x]
            
            if key == UP:
                self.select_y = max(0, self.select_y - 1)
                self.select_x = 0
                change = True
            elif key == DOWN:
                self.select_y = min(3, self.select_y + 1)
                self.select_x = 0
                change = True
            elif key == LEFT:
                self.select_x = max(0, self.select_x - 1)
                change = True
            elif key == RIGHT:
                self.select_x = min(len(cur_row), self.select_x + 1)
                change = True

            if change:
                cur_obj.set_selected(False)

                new_row = self.rows[self.select_y]
                new_row[self.select_x].set_selected(True)
                

    def draw(self, colors):
        # center
        c_s = "■—" * int(config.WIDTH / 2)

        self.scr.addstr(config.CENTER_Y, 0, c_s, colors.WHITE_TEXT)
        
        mt_ss = f"== {self.state_str} =="
        mt_s = f"{mt_ss:^{config.MID_TEXT_WIDTH}}"
        mt_y = config.CENTER_Y
        mt_x = config.MID_TEXT_PADDING

        self.scr.addstr(mt_y, mt_x, mt_s, colors.BLACK_TEXT)

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

        self.player.deck_card.draw(dy, dx, self.scr, colors, len(self.player.deck))

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

        self.enemy.deck_card.draw(dy, dx, self.scr, colors, len(self.enemy.deck))
