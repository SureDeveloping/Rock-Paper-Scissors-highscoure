# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from colorama import Fore, Back
from art import *
import gspread
from google.oauth2.service_account import Credentials
import os
import random
import time
from prettytable import PrettyTable
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('highscore-rpslp')


tprint(" Rock-Paper-Scissors", font="shimrod", chr_ignore=True,)
tprint("  --Extended--", font="utopiab", chr_ignore=True)

print('Welcome to Rock-Paper-Scissors Extended!\n')

user_name = input("Please enter your Name:\n")
# The strip() method ensures that something has to be entered and the isalpha()
# method ensures that no numbers are entered
while not user_name.strip() or not user_name.isalpha():
    user_name = input("The text field must not be left blank"
                      " and only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
print(f"{Fore.YELLOW}{user_name}{Fore.RESET} nice to have you here.\n"
      "This is an extension of the classic game Rock-Paper-Scissors.\n"
      "Compete against the computer and test your luck!\n")

menu_selection = input(f"{Fore.YELLOW}{user_name}{Fore.RESET}, "
                       f"to start the game and play press "
                       f"{Fore.MAGENTA}P{Fore.RESET}.\n"
                       f"To read the rules, press "
                       f"{Fore.MAGENTA}R{Fore.RESET}\n"
                       f"If you want to quit the game press "
                       f"{Fore.MAGENTA}Q{Fore.RESET}.\n"
                       f"If you want to see the highscore list press "
                       f"{Fore.MAGENTA}H{Fore.RESET}.\n").upper()

won_games = 0
lost_games = 0
played_games = 0
drawn_games = 0

highscore = SHEET.worksheet('highscore')

def update_highscore(user_name, played_games, won_games, lost_games, drawn_games):
    """
    A new row is created if no entry has been made since the programme was started. 
    If there is an entry it will be overwirtten
    """
    global highscore

    # Check if data it put the first time into the list
    if played_games == 1:
        # A new row is created and the row number is saved in user a variable, 
        # to be able to overright the data later. 
        highscore.append_row([user_name, played_games, won_games, lost_games, drawn_games])
       

    else:
        # Get number of rows
        num_rows = len(highscore.get_all_values())
        
        # Update data
        highscore.update_cell(num_rows, 1, user_name)
        highscore.update_cell(num_rows, 2, played_games)
        highscore.update_cell(num_rows, 3, won_games)
        highscore.update_cell(num_rows, 4, lost_games)
        highscore.update_cell(num_rows, 5, drawn_games)

   
def print_highscore():
    """
    Print the highscore list.
    """
    os.system('clear')
    print("Highscore List:")
    
    table = highscore.get_all_values()
    # Extract headers
    headers = table.pop(0)  
    print(tabulate(table, headers=headers, tablefmt='pretty'))

    
def start_game():
    """
    The Start game function starts the game.
    It contains the computer_choice function and
    the player-choice function and the Find winner function.
    The next question is asked until the player cancels by pressing quit.
    """
    options_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def computer_choice():
        """
        The random selection of the computer is made here .
        """
        computer_choice = random.choice(options_list)
        print(Fore.BLUE+"Computer choose: "+computer_choice+Fore.RESET)
        return computer_choice

    def player_choice(user_name):
        """
        Here the player makes his selection.
        It is also ensured that non-validated entries are
        taken into account and handled.
        """
        options_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        while True:
            try:
                player_choice_num = int(input(f"{Fore.YELLOW}{user_name}"
                                              f"{Fore.RESET},"
                                              "please choose:\n"
                                              f"{Fore.MAGENTA}1){Fore.RESET} "
                                              "for Rock\n"
                                              f"{Fore.MAGENTA}2){Fore.RESET} "
                                              "for Paper\n"
                                              f"{Fore.MAGENTA}3){Fore.RESET} "
                                              "for Scissors\n"
                                              f"{Fore.MAGENTA}4){Fore.RESET} "
                                              "for Lizard\n"
                                              f"{Fore.MAGENTA}5){Fore.RESET} "
                                              "for Spock\n"
                                              "Your selection: "))-1
                print()
                if player_choice_num not in range(5):
                    print("")
                    raise ValueError("Invalid input."
                                     "Please enter a number between 1 and 5.")

                player_choice = options_list[player_choice_num]
                print(Fore.YELLOW+"You choose: "+player_choice+Fore.RESET)
                return player_choice
            except ValueError as ve:
                print("")
                print("Invalid input. Please enter a number between 1 and 5.")

    def find_winner(computer_choice, player_choice):
        """
        The computer's choice and the player's choice are compared and
        it is decided who has won.
        If both answers are the same, the game is played again.
        """
        global won_games
        global lost_games
        global played_games
        global drawn_games
        if player_choice == computer_choice:
            print("Draw! You have chosen the same item.")
            drawn_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Paper":
            print(Back.RED + "You loose: Paper covers Rock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print(Back.GREEN + "You win: Rock crushes Scissors" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Lizard":
            print(Back.GREEN + "You win: Rock crushes Lizard" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Spock":
            print(Back.RED + "You loose: Spock vaporizes Rock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print(Back.GREEN + "You win: Paper covers Rock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Scissors":
            print(Back.RED + "You loose: Scissors cuts Paper" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Lizard":
            print(Back.RED + "You loose: Lizard eats Paper" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Spock":
            print(Back.GREEN + "You win: Paper disproves Spock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Rock":
            print(Back.RED + "You loose: Rock crushes Scissors" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Paper":
            print(Back.GREEN + "You win: Scissors cuts Paper" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Lizard":
            print(Back.GREEN + "You win: Scissors "
                  "decapitates Lizard" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Spock":
            print(Back.RED + "You loose: Spock smashes Scissors" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Rock":
            print(Back.RED + "You loose: Rock crushes Lizard" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Paper":
            print(Back.GREEN + "You win: Lizard eats Paper" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Scissors":
            print(Back.RED + "You loose: Scissors decapitates "
                  "Lizard" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Spock":
            print(Back.GREEN + "You win: Lizard poisons Spock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Rock":
            print(Back.GREEN + "You win: Spock vaporizes Rock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Paper":
            print(Back.RED + "You loose: Paper disproves Spock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Scissors":
            print(Back.GREEN + "You win: Spock smashes Scissors" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Lizard":
            print(Back.RED + "You loose: Lizard poisons Spock" + Back.RESET)
            lost_games += 1
            played_games += 1

    os.system('clear')
    player_choice_result = player_choice(user_name)
    computer_choice_result = computer_choice()
    find_winner(computer_choice_result, player_choice_result)
    game_end(won_games, lost_games, played_games, drawn_games)


def game_end(won_games, lost_games, played_games, drawn_games):
    """
    After each game the player is asked whether he wants to stop,
    play again or see the highscore list.
    It also ensures that no invalid entries can be made.
    """
    print()
    print(f"{Fore.GREEN}Won games: {won_games}{Fore.RESET}\n"
          f"{Fore.RED}Lost games: {lost_games}{Fore.RESET}\n"
          f"{Fore.BLUE}Played games: {played_games}{Fore.RESET}\n"
          f"{Fore.CYAN}Drawn games: {drawn_games}{Fore.RESET}")
    print()

    # Update highscore after each game
    print("Updating highscoure list...")
    print("")
    update_highscore(user_name, played_games, won_games, lost_games, drawn_games)

    play_again = input(f"Do you want to play again press "
                       f"{Fore.MAGENTA}P{Fore.RESET}.\n"
                       f"If you want to stop, press "
                       f"{Fore.MAGENTA}Q{Fore.RESET}.\n"
                       "Want to see the highscore list press "
                       f"{Fore.MAGENTA}H{Fore.RESET}.\n").upper()
    while True:
        if play_again == 'P':
            start_game()
            break
        elif play_again == 'Q':
            print(f"Thank you {Fore.YELLOW}{user_name}"
                  f"{Fore.RESET} for playing "
                  "Rock-Paper-Scissors Extended!\n"
                  "I look forward to your next game!\n")
            break
        elif play_again == 'H':
            print_highscore()

        else:
            play_again = input(f"Please select {Fore.MAGENTA}"
                               f"P, R or Q{Fore.RESET}. "
                               "All other entries are not "
                               "permitted: \n").upper()


def main_menu(menu_selection, user_name):
    """
    The function provides the selection in the main menu.
    The valid data input is checked and the game is started,
    terminated or the rules are displayed
    according to the user input.
    Before the input is called up, the previous
    entries in the console are deleted.
    """
    os.system('clear')
    while True:
        if menu_selection == 'R':
            rules = ("This version of Rock-Paper-Scissors "
                  "has been made famous\n"
                  "by the TV series "
                  "'The Big Bang Theory'.\n"
                  "The two additional elements make "
                  "it less likely that players "
                  "will choose the same thing,\n"
                  "and providing more variety and excitement.\n"
                  "Rock-Paper-Scissors-Lizard-Spock is a "
                  "game based on luck. "
                  "Choose an item Rock, Paper, Scissors, "
                  "Lizard or Spock.\n"
                  "The computer also makes a random choice. "
                  "Afterwards it is checked who has won.\n"
                  "This is displayed and the scrore is counted up. "
                  "After 10 games you can enter your score in "
                  "the high score list.\n"
                  "Here is a list of which item wins "
                  "against which other item.\n"
                  "\n"
                  "Scissors cuts Paper\n"
                  "Paper covers Rock\n"
                  "Rock crushes Lizard\n"
                  "Lizard poisons Spock\n"
                  "Spock smashes Scissors\n"
                  "Scissors decapitates Lizard\n"
                  "Lizard eats Paper\n"
                  "Paper disproves Spock\n"
                  "Spock vaporizes Rock\n"
                  "Rock crushes Scissors\n")

            for char in rules:
                print(char, end='', flush=True)
                time.sleep(0.02)

            print()

            menu_selection = input("If you want to start the game, press "
                                   f"{Fore.MAGENTA}P{Fore.RESET}.\n"
                                   "If you do not want to play press "
                                   f"{Fore.MAGENTA}Q{Fore.RESET}.\n"
                                   "If you do not want to play press "
                                   f"{Fore.MAGENTA}H{Fore.RESET}.\n"
                                   "If press you want to reloaded "
                                   "the rules press "
                                   f"{Fore.MAGENTA}R{Fore.RESET}.\n"
                                   "All other entries are not "
                                   "permitted: \n").upper()

        elif menu_selection == 'Q':
            print(f"Thank you {Fore.YELLOW}{user_name}"
                  f"{Fore.RESET} for playing "
                  "Rock-Paper-Scissors Extended!\n"
                  "I look forward to your next game!\n")
            break

        elif menu_selection == 'P':
            start_game()
            break

        elif menu_selection == 'H':
            print_highscore()

        else:
            menu_selection = input(f"Please select {Fore.MAGENTA}"
                                   f"P, R or Q{Fore.RESET}. "
                                   "All other entries are not "
                                   "permitted: \n").upper()


main_menu(menu_selection, user_name)
