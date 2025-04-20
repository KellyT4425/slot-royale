import random


def program_banner():

    print()
    print((35 * " ") + "This is" + (35 * " "))
    print(r"""
  _____ _       ___   ______      ____    ___   __ __   ____  _        ___ 
 / ___/| |     /   \ |      |    |    \  /   \ |  |  | /    || |      /  _]
(   \_ | |    |     ||      |    |  D  )|     ||  |  ||  o  || |     /  [_ 
 \__  || |___ |  O  ||_|  |_|    |    / |  O  ||  ~  ||     || |___ |    _]
 /  \ ||     ||     |  |  |      |    \ |     ||___, ||  _  ||     ||   [_ 
 \    ||     ||     |  |  |      |  .  \|     ||     ||  |  ||     ||     |
  \___||_____| \___/   |__|      |__|\_| \___/ |____/ |__|__||_____||_____|
                                                                           
""")


def welcome_user():
    """
    This function asks for an input from the user and displays a welcome message, followed by
    brief instructions on the game.
    """
    name = input("Please enter your name: \n")
    print(f"Welcome {name} to Slot Royale. \U0001F44B \n")
    print("The game is simple, deposit money to your account,")
    print("make a bet and test your LUCK. \U0001F340  \n")
    return name


def exception_error():
    """
    This function will ensure that the users inputs are valid, for name letters/chars are accepted
    for bets and money deposits are correct values in floating-point format.
    """


def user_deposit():
    """
    This function allows the user to input a deposit in other to place bets
    """
    balance = 0
    deposit = input("Please make a deposit: £ \n")
    balance += float(deposit)  # should return 2 decimal places!
    print(f"Your balance is: £{balance} \U0001F4B8 \n")

    return balance


def make_bet(balance):  # NOT IN USE!!!!
    """
    Function to allow user to place a bet before playing, this will be decremented
    from there balance. 
    """
    bet = 0
    bet_amount = input("Please place a bet: £  \n")
    bet += float(bet_amount)  # should return 2 decimal places!
    print(f"Your bet is: £{bet}\n")

    return bet


def decrement_balance(new_balance, bet):
    """
    Function takes the user bet amount away from the users balance.
    """
    result = new_balance - bet
    return result


def slot_machine(bet, new_balance):
    """
    slot machine - takes a tuple of emojis, displays a random
    selection for user. 3 matched = win new balance displayed, if user
    loses balance decremented.
    """
    EMOJIS = ('\U0001F34A', '\U0001F34B', '\U0001F34E', '\U00002B50')

    spin1 = random.choice(EMOJIS)
    spin2 = random.choice(EMOJIS)
    spin3 = random.choice(EMOJIS)

    print(f"| {spin1} | {spin2} | {spin3} |\n")

    while True:
        """
        If spin1, spin2, spin3 == then it is a win. bet * 3, new_balance updated with 
        winnings. else: user lost the round.
        """

        if spin1 == spin2 == spin3:
            print("JACKPOT you won! \U0001F911 \n")
            winnings = bet * 3
            new_balance += winnings
            print(f"Congratulations you WON £{winnings} \U0001F917 \n")

        else:
            print("You lost this round. \U0001f641 \n")

        print(f"Your current balance is: £{new_balance}")

        if new_balance == 0 or new_balance < 0:
            print("You have no more funds! Game Over \U00002620 ")
            print("Restart and top up your Balance! \U0001F929 ")

            break

        go_again = input("Play again? (y/n): \n").lower()
        """
        Provides user with an option to play again after a win or loss. User
        offered to make a new bet.
        """
        if go_again != "y":
            print(
                f"Thank you for Playing your final balance is: £{new_balance} \U0001F44B \n")
            break
        else:
            if go_again != "n":
                new_bet = 0

                new_bet = input("Please place a new bet: £ \n")
                bet += float(new_bet)
                new_balance = new_balance - float(new_bet)

                spin1 = random.choice(EMOJIS)
                spin2 = random.choice(EMOJIS)
                spin3 = random.choice(EMOJIS)

                print(f"| {spin1} | {spin2} | {spin3} |\n")


def main():
    program_banner()
    welcome_user()
    balance = user_deposit()
    bet = make_bet(balance)  # PARAMETER NOT IN USE!!!!!
    new_balance = decrement_balance(balance, bet)
    slot_machine(bet, new_balance)


main()
