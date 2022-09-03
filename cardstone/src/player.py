import random

from src.card import m_One_gen, m_Two_gen, m_Three_gen, m_Four_gen, m_Five_gen

class Player:
    def __init__(self, colors):
        self.deck = [
            next(m_One_gen)
            , next(m_Two_gen)
            , next(m_Three_gen)
            , next(m_Four_gen)
            , next(m_Five_gen)
            , next(m_One_gen)
            , next(m_Two_gen)
            , next(m_Three_gen)
            , next(m_Four_gen)
            , next(m_Five_gen)
            , next(m_One_gen)
            , next(m_Two_gen)
            , next(m_Three_gen)
            , next(m_Four_gen)
            , next(m_Five_gen)
            , next(m_One_gen)
            , next(m_Two_gen)
            , next(m_Three_gen)
            , next(m_Four_gen)
            , next(m_Five_gen)
        ]

        self.board = []
        self.hand = []
        self.graveyard = []
        
        self.cur_mana = 0
        self.max_mana = 0

        self.card_back = colors.WHITE_BACK

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

    def fill_board(self):
        """Testing Only"""
        while len(self.board) < 4:
            self.board.append(self.deck.pop(0))