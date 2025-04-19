import random
import emoji


def welcome_user():
    """
    This function asks for an input from the user and display a welcome message, followed by
    brief instructions on the game.
    """
    name = input("Please enter your name: \n")
    print(f"Welcome {name} this is Slot Royale.\n")
    print("The game is simple, deposit money to your account, make a bet and test your LUCK.")
    print("You have 3 attempts to win, lets get started. \n")
    return name


def exception_error():
    """
    This function will ensure that the users inputs are valid, for name letters/chars are accepted
    for bets and money deposits ints are correct values in floating-point format.
    """


def user_deposit():
    """
    This function allows the user to input a deposit in other to place bets
    """
    balance = 0
    deposit = input("Please make a deposit: £ \n")
    balance += float(deposit)  # should return 2 decimal places!
    print(f"Your balance is: £{balance}")

    return balance


def make_bet(balance):
    """
    Function to allow user to place a bet before playing, this will be decremented
    from there balance. 
    """
    bet = 0
    bet_amount = input("Please place a bet: £  \n")
    bet += float(bet_amount)  # should return 2 decimal places!
    print(f"Your bet is: £{bet}\n")
    # decrement_balance(balance, bet)

    return bet


def decrement_balance(balance, bet):
    """
    Function takes the user bet amount away from the users balance.
    """
    result = balance - bet
    return result


def slot_machine(bet, balance, new_balance):
    EMOJIS = ('\U0001F34A', '\U0001F34B', '\U0001F34E', '\U00002B50')

    spin1 = random.choice(EMOJIS)
    spin2 = random.choice(EMOJIS)
    spin3 = random.choice(EMOJIS)

    print(f"| {spin1} | {spin2} | {spin3} |\n")

    while True:

        if spin1 == spin2 == spin3:
            print("JACKPOT you won! \U0001F911 \n")
            winnings = bet * 3
            balance += winnings
            print(f"Congratulations you WON {winnings}\n")

        else:
            print("You lost this round.")
            decrement_balance(balance, bet)

        print(f"Your current balance is: £{new_balance}")

        if balance == 0:
            print("You have no more funds! Game Over")
            # make_bet(balance)
            break

        go_again = input("Play again? (y/n): \n").lower()
        if go_again != "y":
            print(
                f"Thank you for Playing your final balance is: {new_balance}")
            break


def main():
    welcome_user()
    balance = user_deposit()
    bet = make_bet(balance)
    new_balance = decrement_balance(balance, bet)
    slot_machine(bet, balance, new_balance)


main()
