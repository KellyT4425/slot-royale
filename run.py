import random

def welcome_user():
    """
    This function asks for an input from the user and display a welcome message, followed by
    brief instructions on the game.
    """
    name = input("Please enter your name: \n")
    print(f"Welcome {name} this is Slot Royale.\n")
    print("The game is simple, deposit money to your account, make a bet and test your LUCK.")
    print("You have 3 attempts to win, lets get started.")
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
    balance += float(deposit) # should return 2 decimal places!
    print(f"Your balance is: £{balance}")
    
    return balance

def make_bet():
    """
    Function to allow user to place a bet before playing, this will be decremented
    from there balance. 
    """
    bet = 0
    bet_amount = input("Please place a bet: £  \n")
    bet += float(bet_amount) # should return 2 decimal places!
    print(f"Your bet is: £{bet}")

    return bet




def main():
   welcome_user() 
   user_deposit()
   make_bet()


main()