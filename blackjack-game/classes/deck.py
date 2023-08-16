from .card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ["hearts", "clubs", "spades", "diamonds"]
        ranks = [{ 'rank': "A", "value": 11 }, { 'rank': "K", "value": 10 }, { 'rank': "Q", "value": 10 }, 
                { 'rank': "J", "value": 10 }, { 'rank': "9", "value": 9 }, { 'rank': "8", "value": 8 },
                { 'rank': "7", "value": 7 }, { 'rank': "6", "value": 6 }, { 'rank': "5", "value": 5 },
                { 'rank': "4", "value": 4 }, { 'rank': "3", "value": 3 }, { 'rank': "2", "value": 2 }
                ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, amount: int = 1) -> list:
        cards_dealt = []
        for x in range(amount):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)

        return cards_dealt
