import os
import time
import sys
import gspread
from google.oauth2.service_account import Credentials
from questions import question_list

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ci_project_portfolio_3")

sales = SHEET.worksheet("sales")
data = sales.get_all_values()

def start_quiz():
    """ Loads the questions and validates the users answer """
    score = 0
    for question in question_list:
        user_answer = input(question.question).capitalize()
        if user_answer == question.answer:
            score += 1
            print("Correct answer!")
        else:
            print("Incorrect answer")
    print("Quiz finished")


def clear_terminal():
    """ Clears the terminal """
    os.system('clear')


def exit_game():
    """ Exits the game """
    print("Thank you for playing\n")
    print("Shutting the program down...\n")
    time.sleep(2)
    print("Program shutdown successfully")
    sys.exit()


def main_menu():
    """ Displays the main menu to the user that allows them to navigate the application """
    print("Welcome to the main menu")
    user_input = input("A) Start the Quiz\nB) Exit the game\n").capitalize()
    if user_input == ("A"):
        print("Great stuff, starting a new quiz now...")
        time.sleep(2)
        clear_terminal()
        start_quiz()
    if user_input == ("B"):
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        exit_game()

print("Welcome to the F1 quiz!")
name = input("Please enter your name: ")

main_menu()
