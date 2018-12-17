from os import name as os_name, system as os_system
from time import sleep
from player import Player
from blackjack import Blackjack


def clear():
    if os_name == 'nt':
        os_system('cls')
    else:
        os_system('clear')


def initial_message():
    print("Welcome to the Blackjack game dear stranger!")


def ask_to_start():
    answer = input("Do You want to start a game? (y) ")
    if answer.lower() == 'y':
        start_new_game()
    else:
        print("Thanks for hanging out, bye o/")


def start_new_game():

    clear()
    player = create_new_player()
    clear()
    create_new_game(player=player)


def create_new_player():
    name = input("What's Your name stranger? ")
    player = Player(name)
    return player


def create_new_game(player):
    print(player.info())
    bet = input("How much do You want to bet? ")
    bet_validate(player=player, bet=bet)
    game = Blackjack(player=player, bet=int(bet))
    play_blackjack(player=player, game=game)


def bet_validate(player, bet):
    bet_type_validate(player=player, bet=bet)
    bet_account_state_validate(player=player, bet=bet)


def bet_type_validate(player, bet):
    try:
        int(bet)
    except ValueError:
        clear()
        print('Sorry, this is not a number!')
        create_new_game(player)


def bet_account_state_validate(player, bet):
    if int(bet) > player.money:
        clear()
        print("Sorry, You can't bet that much!")
        create_new_game(player)


def play_blackjack(player, game):
    print('Deck is being shuffled....')
    game.shuffle_dec()
    sleep(2)
    clear()
    initial_table(game=game)
    while True:
        clear()
        game.setup_table()
        if game.player_cards_sum[0] == 21:
            player_won(player, game)
            break
        elif game.player_cards_sum[0] > 21:
            player_lost(player, game)
            break
        choice = input("Do You want to hit ? (y/n) ")
        if choice.lower() == 'y':
            game.player_hits()
            game.player_cards_sum = sum_of_cards(game.player_cards)
        else:
            game.croupier_cards_sum[0] = 0
            while True:
                if game.croupier_cards_sum[0] < 21 and game.croupier_cards_sum[0] <= game.player_cards_sum[0]:
                    game.croupier_hits()
                    game.croupier_cards_sum = sum_of_cards(game.croupier_cards)
                    clear()
                    game.setup_table()
                else:
                    if game.croupier_cards_sum[0] < game.player_cards_sum[0] or game.croupier_cards_sum[0] > 21:
                        player_won(player, game)
                    else:
                        player_lost(player, game)
                    break

            break


def sum_of_cards(hand):
    cards_sum = [0, 0, 0, 0]
    for card in hand:
        if card in range(2, 11):
            cards_sum[0] += card
        elif card in ['Jack', 'Queen', 'King']:
            cards_sum[0] += 10
        elif card == 'Ace' and cards_sum[1] == 0:
            cards_sum[1] = 1
            cards_sum[2] = 11
        elif card == 'Ace' and cards_sum[1] > 0:
            cards_sum[1] = 2
            cards_sum[2] = 12
            cards_sum[3] = 22
    if cards_sum[1] > 0 and cards_sum[3] == 0:
        cards_sum[1] += cards_sum[0]
        cards_sum[2] += cards_sum[0]
        try:
            cards_sum[0] = max(card for card in cards_sum[1:3] if card <= 21)
        except ValueError:
            cards_sum[0] = min(cards_sum[1:3])
    elif cards_sum[1] > 0 and cards_sum[3] > 0:
        cards_sum[1] += cards_sum[0]
        cards_sum[2] += cards_sum[0]
        cards_sum[3] += cards_sum[0]
        try:
            cards_sum[0] = max(card for card in cards_sum[1:4] if card <= 21)
        except ValueError:
            cards_sum[0] = min(cards_sum[1:3])

    return cards_sum


def initial_table(game):
    game.initial_cards()
    game.player_cards_sum = sum_of_cards(game.player_cards)
    game.setup_table()


def player_won(player, game):
    print('Congratulations, You have won!')
    player.add_money(game.bet)
    if input('Do You want to play again? (y) ').lower() == 'y':
        clear()
        create_new_game(player)
    else:
        print('See You again!')


def player_lost(player, game):
    print('You lost!')
    player.remove_money(game.bet)
    if input('Do You want to play again? (y) ').lower() == 'y':
        clear()
        create_new_game(player)
    else:
        print('See You again!')


if __name__ == '__main__':
    clear()
    initial_message()
    ask_to_start()
