import random
import os
import time

# GLOBAL VARIABLES ---------------------------------------------------->
thisList = []  # empty list, append player bets on each spin and if they
# won the win amount ie:  1. bet: 10 win: 0  2. bet: 20 win: 60
bet_total = 0  # store the total players bets
total_spins = 0  # amount of spins
total_winnings = 0  # overall winnings


def clear_console():
    """
    using os.system python library. Function allows for clearing the console
    at different stages of the program.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()


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


program_banner()


def welcome_user():
    """
    This function asks for an input from the user and
    displays a welcome message, followed by brief
    instructions on the game.
    """
    name = get_valid_name()
    print(f"Welcome {name} to Slot Royale. \U0001F44B \n")
    print("The game is simple, deposit money to your account,")
    print("make a bet and test your LUCK. \U0001F340  \n")

    return name


def get_valid_name():
    """
    Asks user for valid name input.
    If invalid it informs the user and asks for
    letters only and loops, asking user for input again.
    """
    while True:
        # Removes any leading or trailing spaces from the input
        name = input("Please enter your name: \n").strip()
        # checks for letters, removes extra spaces.
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name. Please use letters only.\n")


def get_valid_float(prompt, min_value=0.01, max_value=None):
    """
    Ensure the user is inputing a valid number or float
    like 10 or 10.00. This function is used in deposits and bets.
    """
    while True:
        try:
            # ensures flexibilty using input prompt
            value = float(input(prompt))
            # checks if users value input is < min_value default parameter.
            if value < min_value:
                print(
                    f"Please enter an amount greater or"
                    f"equal to £{min_value:.2f}.\n")
            # checks that max_value is not None and that the user value is
            # > min_value such as users balance. parameter is optional if
            # user does not provide a max_value it will default to None.
            elif max_value is not None and value > max_value:
                print(
                    f"You exceeded your balance £{max_value:.2f}.\n")
            else:
                return round(value, 2)  # rounds result to 2 decimal places.
        except ValueError:
            print("Invalid input. Please enter a number like 10 or 10.00\n")


def get_valid_input(prompt):
    """
    Makes sure the users input is either "y" or "n".
    Any other input is handled by an invalid input, error message.
    """
    while True:
        user_input = input(prompt).lower()
        valid_input = ("y", "n")
        if user_input in valid_input:
            return user_input
        else:
            print("Invalid input, please enter either y or n!")


def add_stats(bet, win):
    """
    This function appends the provided bet and win amounts to the global list.
    The list keeps track of all betting rounds. It then updates the global
    bet_total.
    """
    global bet_total, total_winnings
    thisList.append([bet, win])
    bet_total += bet
    return bet_total


def calculate_stats():
    """
    Calculates and updates the total slot machine stats for the player.

    It computes the total number of spins and winnings, based off
    of the values stored in the global thisList = [].

    It then updates total_spins and total_winnings.

    """
    global total_spins, total_winnings
    total_spins = len(thisList)
    total_winnings = 0
    for _, win in thisList:
        total_winnings += win


def show_stats():
    """
    This function display the stats to the user when they respond "y" from
    an input prompt.
    """
    print(f"Total spins: {total_spins}")
    print(f"Total bets: £{bet_total:.2f}")
    print(f"Total winnings: £{total_winnings:.2f}")


def user_deposit():
    """
    This function allows the user to input a deposit in order
    to place bets. It is using the get_valid_float() to
    validate user input.  As specified above
    with value = float(input(prompt))
    """
    balance = 0
    deposit = get_valid_float("Please make a deposit: £ \n")
    print()
    balance += deposit

    return balance


def make_bet(current_balance):
    """
    Function to allow user to place a bet before playing,
    this will be decremented from there balance.
    It also ensures that the user does not over bet there balance
    """
    while True:
        # Using the get_valid_float() it is assigning the max_value
        # parameter to the current_balance ensuring the user does
        # not over bet there current balance as it is set to max.
        bet = get_valid_float(
            f"Please place a bet (max £{current_balance:.2f}): £\n",
            max_value=current_balance)
        print()
        return bet


def decrement_balance(new_balance, bet):
    """
    Function takes the user bet amount away from the users new balance.
    """
    result = new_balance - bet
    return result


def slot_machine(bet, new_balance):
    """
    slot machine - takes a tuple of emojis, displays a random
    selection for user. Determines win or loss.
    """
    EMOJIS = ('\U0001F34A', '\U0001F34B', '\U0001F34E', '\U00002B50')

    spin1 = random.choice(EMOJIS)
    spin2 = random.choice(EMOJIS)
    spin3 = random.choice(EMOJIS)

    while True:
        """
        If spin1, spin2, spin3 == then it is a win. bet * 3,
        new_balance updated with winnings. else: user lost the round.
        """
        new_balance = decrement_balance(
            new_balance, bet)  # decrements bet from balance.

        print("Spinning the reels...", end="", flush=True)
        print()
        for _ in range(20):  # Number of spin cycles
            spin1 = random.choice(EMOJIS)
            spin2 = random.choice(EMOJIS)
            spin3 = random.choice(EMOJIS)
            print(f"\r| {spin1} | {spin2} | {spin3} |", end="", flush=True)
            time.sleep(0.1)  # Delay between "spins"

        print()  # Move to next line after final spin result

        if spin1 == spin2 == spin3:
            print("JACKPOT you won! \U0001F911 \n")
            winnings = bet * 3
            new_balance += winnings
            add_stats(bet, winnings)
            print(f"Congratulations you WON £{winnings:.2f} \U0001F917 \n")
        else:  # lost round, display balance, moves to play_again.
            print("You lost this round. \U0001f641 \n")
            add_stats(bet, 0)
            print(f"Your current balance is: £{new_balance:.2f} \n")

        calculate_stats()  # calls calculate_stats function above.
        # gets valid input from user.
        stats = get_valid_input("Would you like to see your stats: (y/n)  \n")
        if stats == "y":
            show_stats()

        if new_balance == 0:  # Once at 0 game is over
            print("You have no more funds! Game Over \U00002620 ")

            # Top-up option added when players balance is 0, means that player
            # doesnt have to restart the program to continue playing.
            top_up = get_valid_input(
                "Would you like to make a deposit?: (y/n)  \U0001F929 \n")
            print()

            if top_up == "y":
                deposit_amount = user_deposit()
                new_balance += deposit_amount
                print(f"Your new balance is: £{new_balance:.2f} \n")
                print()

            elif top_up == "n":
                print("Thank you for playing, Hope to see you again soon!")

                break

        go_again = get_valid_input("Play again?: (y/n) \n")

        print()
        """
        Provides user with an option to play again after a win or loss.
        User offered to make a new bet.
        """
        if go_again == "y":

            # asking for new bet from user to continue playing.
            clear_console()
            bet = make_bet(new_balance)

            spin1 = random.choice(EMOJIS)
            spin2 = random.choice(EMOJIS)
            spin3 = random.choice(EMOJIS)

        if go_again == "n":
            print(
                f"Thank you for Playing your balance is: "
                f"£{new_balance:.2f} \U0001F44B \n")

            break


def main():
    welcome_user()
    balance = user_deposit()
    bet = make_bet(balance)
    slot_machine(bet, balance)


main()
