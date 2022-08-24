# Card configs
CARD_WIDTH          = 20
CARD_HEIGHT         = 7
OUTLINE_OFFSET_Y    = 1
OUTLINE_OFFSET_X    = 1
TITLE_WIDTH         = CARD_WIDTH
MANA_OFFSET_Y       = CARD_HEIGHT - 1
TEXT_OFFSET_Y       = 2
TEXT_OFFSET_X       = 1
TEXT_WIDTH          = CARD_WIDTH - 2
TEXT_HEIGHT         = 3
FACTION_OFFSET_Y    = 5

# card.Minion configs
STAT_OFFSET_Y     = CARD_HEIGHT - 1

# Board configs
CARD_SPACE          = CARD_WIDTH + 4

# screen configs
WIDTH               = (CARD_SPACE * 5) + (CARD_SPACE + 4) + (12) # (hand/field) + (deck/graveyard) + (mana bar)
HEIGHT              = 40
FPS                 = 6
FPS_RATIO           = 1 / FPS