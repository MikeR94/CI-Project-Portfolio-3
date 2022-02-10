""" Main file to run the F1 quiz """


from datetime import datetime
import os
import time
import sys
import random
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from print import cyan_string, green_string, magenta_string, red_string, white_string, yellow_string, blue_string
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
facts = SHEET.worksheet("facts")
fact_data = facts.get_all_values()
feedback = SHEET.worksheet("feedback")
nowdate = datetime.now()
date = nowdate.strftime("%d/%m/%Y")


def start_quiz(selected_difficulty):
    """ Loads the questions and validates the users answer """
    score = 0
    correct = 0
    incorrect = 0
    questions = random.sample(selected_difficulty, 5)
    for question in questions:
        while True:
            user_answer = input(question.question).capitalize()
            if user_answer not in {"A", "B", "C"}:
                print("Invalid input! You can attempt the question again\n")
            else:
                break
        if user_answer == question.answer:
            print("Correct answer!\n")
            time.sleep(2)
            correct += 1
            if selected_difficulty == easy_question_list:
                difficulty_selected = "Easy"
                score += 5
            elif selected_difficulty == medium_question_list:
                difficulty_selected = "Medium"
                score += 10
            elif selected_difficulty == hard_question_list:
                difficulty_selected = "Hard"
                score += 20
        else:
            incorrect += 1
            print("Incorrect answer\n")
            time.sleep(2)
    print("Great stuff, " + name + " You've managed to answer all the questions!\n")
    print("You scored " + str(score) + " points, answering " + str(correct) + " correct and " + str(incorrect) + " incorrect\n")
    time.sleep(2)
    print("Please wait, adding your score to the leaderboard...\n")
    leaderboard.append_row(values=[name, score, correct, incorrect, difficulty_selected, date])
    leaderboard.sort((2, 'des'))
    time.sleep(2)
    print("Leaderboard updated successfully!\n")
    quick_menu()


def quick_menu():
    """Small navigation menu for the user"""
    print("----------------------")
    while True:
        user_input = (input("A) Return to main menu B) Exit game\n ").capitalize())
        if user_input not in {"A", "B"}:
            print("Invalid input! Please enter either A, B\n")
        else:
            break
    if user_input == ("A"):
        print("Understood " + name + ", redirecting back to the main menu...")
        time.sleep(2)
        clear_terminal()
        main_menu()
    if user_input == ("B"):
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        exit_game()


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


def show_leaderboards():
    """ Shows the leaderboards to the user """
    leaderboard.sort((2, 'des'))
    print(tabulate(data[0:10], tablefmt='fancy_grid'))
    quick_menu()


def show_game_stats():
    """Shows the game stats"""
    games_played = leaderboard.row_count - 1
    print(f"Overall games played: {games_played}\n")
    total_points = []
    for item in leaderboard.col_values(2):
        if item.isdigit():
            total_points.append(int(item))
    print(f"Overall points accumulated: {sum(total_points)}\n")
    total_correct = []
    for item in leaderboard.col_values(3):
        if item.isdigit():
            total_correct.append(int(item))
    print(f"Overall correct questions answered: {sum(total_correct)}\n")
    total_incorrect = []
    for item in leaderboard.col_values(4):
        if item.isdigit():
            total_incorrect.append(int(item))
    print(f"Overall incorrect questions answered: {sum(total_incorrect)}\n")
    quick_menu()


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


def show_game_rules():
    """ Displays the game rules to the user """
    print("Currently under construction\n")
    quick_menu()


def show_fact():
    """ Displays a random F1 fact to the user """
    random_fact = get_random_fact()
    print(random_fact)
    quick_menu()


def get_random_fact():
    """ Stores all facts in a list, picks one at random and returns it as a string"""
    fact_list = []
    for i in fact_data:
        fact_list.append(i)
    load_fact = random.choice(fact_list)
    return ''.join(load_fact)


def submit_feedback():
    """ Allows the user to submit feedback """
    print(name + ", please submit your feedback below\n")
    print("If you wish to leave this screen before submitting a message, please click the run program button below\n")
    user_feedback = input("Enter feedback: ")
    print()
    print("Thank you for your feedback, uploading now...\n")
    time.sleep(2)
    feedback.append_row(values=[name, user_feedback, date])
    print("Feedback uploaded successfully!\n")
    quick_menu()


def main_menu():
    """ Displays the main menu to the user that allows them to navigate the application """
    print("Welcome to the main menu, " + name + "!\n")
    red_string("Welcome!")
    print("Please select an option from the menu\n")
    user_input = input("A) Start the Quiz\nB) View the leaderboards\nC) View game statistics\nD) View game rules\nE) View an F1 fact\nF) Submit feedback\nG) Exit the game\n").capitalize()
    while True:
        if user_input not in {"A", "B", "C", "D", "E", "F", "G"}:
            print("Invalid input! Please enter either A, B, C, D, E, F or G\n")
            time.sleep(1)
            clear_terminal()
            main_menu()
        else:
            break
    if user_input == ("A"):
        print("Great stuff, starting a new quiz now...")
        time.sleep(2)
        clear_terminal()
        select_difficulty()
    if user_input == ("B"):
        print("Loading the leaderboards...")
        time.sleep(2)
        clear_terminal()
        show_leaderboards()
    if user_input == ("C"):
        print("Loading the game statistics...")
        time.sleep(2)
        clear_terminal()
        show_game_stats()
    if user_input == ("D"):
        print("Loading the game rules...")
        time.sleep(2)
        clear_terminal()
        show_game_rules()
    if user_input == ("E"):
        print("Loading the F1 fact display...")
        time.sleep(2)
        clear_terminal()
        show_fact()
    if user_input == ("F"):
        print("Loading submit feedback...")
        time.sleep(2)
        clear_terminal()
        submit_feedback()
    if user_input == ("G"):
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        exit_game()

print("Welcome to the F1 quiz!")
red_string("Welcome".center(50))
green_string("Welcome")
yellow_string("Welcome")
blue_string("Welcome")
magenta_string("Welcome")
cyan_string("Welcome")
white_string("Welcome")

while True:
    name = input("Please enter your name: ")
    if len(name) > 7 or name.isspace() or name =="":
        print('Please enter a name that is 7 characters or less\n')
    else:
        break
time.sleep(2)
clear_terminal()

main_menu()
