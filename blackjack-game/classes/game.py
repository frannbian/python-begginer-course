from .deck import Deck
from .hand import Hand

class Game:
    def play(self) -> None:
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many play do you wanna play? "))
            except:
                print("You must enter a Number")
        
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            dealer_hand = Hand(True)
            
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(dealer_hand, player_hand):
                continue
            
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Pease choice 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Pease choice 'Hit' or 'Stand' (or h/s): ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal())
                    print(player_hand.display())
                    
                    
            if self.check_winner(dealer_hand, player_hand):
                continue
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer_cards = True)
            
            if self.check_winner(dealer_hand, player_hand):
                continue
            
            print("Final Result")
            print(f"Your hand {player_hand_value}")
            print(f"Dealer hand {dealer_hand_value}")
            
            self.check_winner(dealer_hand, player_hand, True)
            
        print("\nThanks for playing")            
                    
    def check_winner(self, dealer_hand, player_hand, game_over = False) -> bool:
        if not game_over:
            if player_hand.get_value() > 21:
                print("Dealer wins! You has more than 21")
                return True
            elif dealer_hand.get_value() > 21:
                print("You wins! Dealer has more than 21")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("It's a tie! Both has blackjack")
                return True
            elif player_hand.is_blackjack():
                print("You win! You have blackjack")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer win! Dealer has blackjack")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! You has more than dealer")
            elif dealer_hand.get_value() > player_hand.get_value():
                print("Dealer win! Dealer has more than you")
            else:
                print("It's a Tie! Both have the same value")
        return False