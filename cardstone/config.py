# Card configs
CARD_WIDTH          = 20
CARD_HEIGHT         = 7
OUTLINE_OFFSET_Y    = 1
OUTLINE_OFFSET_X    = 1
TITLE_WIDTH         = CARD_WIDTH
MANA_OFFSET_Y       = CARD_HEIGHT - 1
TEXT_OFFSET_Y       = 2
TEXT_OFFSET_X       = 1
TEXT_WIDTH          = CARD_WIDTH - (TEXT_OFFSET_X * 2)
TEXT_HEIGHT         = 3
FACTION_OFFSET_Y    = 5

# card.Minion configs
STAT_OFFSET_Y       = CARD_HEIGHT - 1

# Game configs
CARD_SPACE_PADDING_X        = 2
CARD_SPACE                  = CARD_WIDTH + (CARD_SPACE_PADDING_X * 2)
PLAYER_BOTTOM_Y             = (CARD_HEIGHT * 3) + (9) # (hand/field/field) + spacer
DECK_X                      = (CARD_SPACE * 5) + 4 + CARD_SPACE_PADDING_X # (hand) + (spacing)
PLAYER_DECK_TEXT_OFFSET_Y   = 2
DECK_TEXT_OFFSET_X          = 3 
DECK_TEXT_WIDTH             = CARD_WIDTH - (DECK_TEXT_OFFSET_X * 2)
PLAYER_DECK_COUNT_OFFSET_Y  = 4
DECK_COUNT_OFFSET_X         = 5
DECK_COUNT_WIDTH            = CARD_WIDTH - (DECK_COUNT_OFFSET_X * 2)
MANA_BAR_OFFSET_Y = 2
MANA_BAR_OFFSET_X = 2

# screen configs
WIDTH               = (CARD_SPACE * 5) + (CARD_SPACE + 4) + (12) # (hand/field) + (deck/graveyard) + (mana bar)
HEIGHT              = 39
FPS                 = 6
FPS_RATIO           = 1 / FPS