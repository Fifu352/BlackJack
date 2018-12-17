"""
This is a file consisting of blackjack class
"""
from random import shuffle


class Blackjack:


    def __init__(self, player, bet):
        """

        :param player: Player playing a blackjack game passed as object
        :param bet: A value of the bet that the player made for particular game
        :type player: object
        :type bet:int
        """
        self.player = player
        self.bet = bet
        self.croupier_cards = []
        self.croupier_cards_sum = ['?', 0, 0, 0]
        self.player_cards = []
        self.player_cards_sum = [0, 0, 0, 0]
        self.deck = [card for card in range(2, 11) for _ in range(4)]
        self.deck.extend(['Ace', 'Jack', 'Queen', 'King'] * 4)

    def shuffle_dec(self):
        shuffle(self.deck)

    def setup_table(self):
        print(
            f"Croupier: "
            
            f"""{
            self.croupier_cards_sum[0] if self.croupier_cards_sum[1] == 0 else ''
            }"""
            
            f"""{
            'You have Ace! ' + 
            str(self.croupier_cards_sum[1]) + ' or ' +
            str(self.croupier_cards_sum[2]) 
            if self.croupier_cards_sum[1] > 0 and self.croupier_cards_sum[3] == 0 else ''
            }"""
            
            f"""{
            'You have Two Aces! ' + 
            str(self.croupier_cards_sum[1]) + ' or ' + 
            str(self.croupier_cards_sum[2]) + ' or ' +
            str(self.croupier_cards_sum[3]) 
            if self.croupier_cards_sum[3] > 0 else ''
            }"""
        )
        print(f"{'  '.join(map(str, self.croupier_cards)) if self.croupier_cards_sum[0] != '?' else str(self.croupier_cards[0]) + ' ?'}")
        print(f"\n\n\n\n{'  '.join(map(str, self.player_cards))}")
        print(
            f"Player: "
            
            f"""{
            self.player_cards_sum[0] if self.player_cards_sum[1] == 0 else ''
            }"""
            
            f"""{
            'You have Ace! ' + 
            str(self.player_cards_sum[1]) + ' or ' +
            str(self.player_cards_sum[2]) 
            if self.player_cards_sum[1] > 0 and self.player_cards_sum[3] == 0 else ''
            }"""
            
            f"""{
            'You have Two Aces! ' + 
            str(self.player_cards_sum[1]) + ' or ' + 
            str(self.player_cards_sum[2]) + ' or ' +
            str(self.player_cards_sum[3]) 
            if self.player_cards_sum[3] > 0 else ''
            }"""
        )

    def initial_cards(self):
        self.croupier_cards.append(self.deck.pop())
        self.croupier_cards.append(self.deck.pop())
        self.player_cards.append(self.deck.pop())
        self.player_cards.append(self.deck.pop())

    def player_hits(self):
        self.player_cards.append(self.deck.pop())

    def croupier_hits(self):
        self.croupier_cards.append(self.deck.pop())
