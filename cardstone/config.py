# Card configs
CARD_WIDTH          = 20
CARD_HEIGHT                 = 7
OUTLINE_OFFSET_Y            = 1
OUTLINE_OFFSET_X            = 1
TITLE_WIDTH                 = CARD_WIDTH
MANA_OFFSET_Y               = CARD_HEIGHT - 1
TEXT_OFFSET_Y               = 2
TEXT_OFFSET_X               = 1
TEXT_WIDTH                  = CARD_WIDTH - (TEXT_OFFSET_X * 2)
TEXT_HEIGHT                 = 3
FACTION_OFFSET_Y            = 5

# Minion(Card) configs
STAT_OFFSET_Y               = CARD_HEIGHT - 1

# Game configs
CARD_SPACE_PADDING          = 2
CARD_SPACE                  = CARD_WIDTH + (CARD_SPACE_PADDING * 2)
PLAYER_BACK_Y               = ((CARD_HEIGHT + CARD_SPACE_PADDING) * 3) + (9) # (hand/board/board) + (center)
PLAYER_FRONT_Y              = ((CARD_HEIGHT + CARD_SPACE_PADDING) * 2) + (9) # (hand/board/board) + (center)
ENEMY_BACK_Y                = 0
ENEMY_FRONT_Y               = CARD_HEIGHT + CARD_SPACE_PADDING
DECK_X                      = (CARD_SPACE * 5) + 4 + CARD_SPACE_PADDING # (hand) + (spacing) + (padding)
ENEMY_DECK_TEXT_Y           = ENEMY_BACK_Y + 2
PLAYER_DECK_TEXT_Y          = PLAYER_BACK_Y + 2
DECK_TEXT_PADDING_X           = 3
DECK_TEXT_X                 = DECK_X + DECK_TEXT_PADDING_X
DECK_TEXT_WIDTH             = CARD_WIDTH - (DECK_TEXT_PADDING_X * 2)
DECK_COUNT_PADDING_X        = 5
ENEMY_DECK_COUNT_Y          = ENEMY_BACK_Y + 4
PLAYER_DECK_COUNT_Y         = PLAYER_BACK_Y + 4
DECK_COUNT_X                = DECK_X + DECK_COUNT_PADDING_X
DECK_COUNT_WIDTH            = CARD_WIDTH - (DECK_COUNT_PADDING_X * 2)
MANA_BAR_OFFSET_Y = 2
MANA_BAR_OFFSET_X = 2

# screen configs
WIDTH                       = (CARD_SPACE * 5) + (CARD_SPACE + 4) + (12) # (hand/board) + (deck/portrait) + (mana bar)
HEIGHT                      = ((CARD_HEIGHT + CARD_SPACE_PADDING) * 4) + (9) # (hand/board/board/hand) + (center)
FPS                         = 60
FPS_RATIO                   = 1 / FPS
ANIM_FPS                    = 12
ANIM_FPS_RATIO              = 1 / ANIM_FPS

# setting configs
SHOW_DEV_STATS              = False