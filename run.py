import os
import time
import sys
import random
import gspread
from google.oauth2.service_account import Credentials
from questions import easy_question_list
from questions import medium_question_list
from questions import hard_question_list


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ci_project_portfolio_3")
leaderboard = SHEET.worksheet("leaderboard")
data = leaderboard.get_all_values()


def start_quiz(selected_difficulty):
    """ Loads the questions and validates the users answer """
    score = 0
    questions = random.sample(selected_difficulty, 5)
    for question in questions:
        user_answer = input(question.question).capitalize()
        if user_answer == question.answer:
            if selected_difficulty == easy_question_list:
                score += 5
            elif selected_difficulty == medium_question_list:
                score += 10
            elif selected_difficulty == hard_question_list:
                score += 20
        else:
            print("Incorrect answer")
    print("Please wait, adding your score to the leaderboard...\n")
    leaderboard.append_row(values=[name, score])
    time.sleep(2)
    print("Leaderboard updated successfully!\n")


def select_difficulty():
    """ Allows the user to select a difficulty """
    print("Please select a difficulty\n")
    user_input = input("A) Easy\nB) Medium\nC) Hard\n").capitalize()
    if user_input == ("A"):
        print("Loading easy questions...")
        time.sleep(2)
        clear_terminal()
        start_quiz(easy_question_list)
    elif user_input == ("B"):
        print("Loading medium questions...")
        time.sleep(2)
        clear_terminal()
        start_quiz(medium_question_list)
    elif user_input == ("C"):
        print("Loading hard questions...")
        time.sleep(2)
        clear_terminal()
        start_quiz(hard_question_list)
    else:
        print("Please enter either A, B or C")
        time.sleep(2)
        clear_terminal()
        select_difficulty()


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
        select_difficulty()
    if user_input == ("B"):
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        exit_game()

print("Welcome to the F1 quiz!")
name = input("Please enter your name: ")

main_menu()
