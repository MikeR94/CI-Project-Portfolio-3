""" Main file to run the F1 quiz """


from datetime import datetime
import os
import time
import sys
import random
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from print import cyan_string, formula_1_text, green_string, magenta_string, multiple_blank_lines
from print import red_string, white_string, yellow_string, blank_line, solid_line
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


def days_to_new_season():
    """ Test """
    futuredate = datetime.strptime('Mar 18 2022  00:00', '%b %d %Y %H:%M')
    count = int((futuredate-nowdate).total_seconds())
    days = count//86400
    number_of_days = "{} days".format(days)
    if days == 0:
        return green_string("The F1 2022 season has started!".center(80))
    return red_string(f"Days left until F1 2022 Season: {number_of_days}".center(80))


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
                yellow_string("Invalid input! You can attempt the question again\n")
            else:
                break
        if user_answer == question.answer:
            green_string("Correct answer!\n")
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
            red_string("Incorrect answer\n")
            time.sleep(2)
    white_string("Great stuff, " + name + " You've managed to answer all the questions!\n")
    white_string("You scored " + str(score) + " points, answering " + str(correct) + " correct and " + str(incorrect) + " incorrect\n")
    time.sleep(2)
    magenta_string("Please wait, adding your score to the leaderboard...\n")
    leaderboard.append_row(values=[name, score, correct, incorrect, difficulty_selected, date])
    leaderboard.sort((2, 'des'))
    time.sleep(2)
    green_string("Leaderboard updated successfully!\n")
    quick_menu()


def quick_menu(centered=False):
    """Small navigation menu for the user"""
    if centered:
        while True:
            cyan_string("A) Return to main menu B) Exit game".center(80))
            user_input = input().capitalize()
            if user_input not in {"A", "B"}:
                yellow_string("Invalid input! Please enter either A or B")
            else:
                break
        if user_input == ("A"):
            magenta_string(f"Understood {name}, redirecting back to the main menu...".center(80))
            time.sleep(2)
            clear_terminal()
            main_menu()
        if user_input == ("B"):
            magenta_string("Exiting the game...".center(80))
            time.sleep(2)
            clear_terminal()
            exit_game()
    else:
        while True:
            cyan_string("A) Return to main menu B) Exit game")
            user_input = input().capitalize()
            if user_input not in {"A", "B"}:
                yellow_string("Invalid input! Please enter either A or B\n")
            else:
                break
        if user_input == ("A"):
            magenta_string("Understood " + name + ", redirecting back to the main menu...")
            time.sleep(2)
            clear_terminal()
            main_menu()
        if user_input == ("B"):
            magenta_string("Exiting the game...")
            time.sleep(2)
            clear_terminal()
            exit_game()


def fact_menu():
    """Small navigation menu for the user"""
    while True:
        cyan_string(
            'A) Return to main menu '
            'B) Exit game '
            'C) Load new fact\n'.center(80))
        user_input = input().capitalize()
        if user_input not in {"A", "B", "C"}:
            yellow_string("Invalid input! Please enter either A, B, or C \n".center(80))
        else:
            break
    if user_input == ("A"):
        magenta_string(f"Understood {name}, redirecting back to the main menu...".center(80))
        time.sleep(2)
        clear_terminal()
        main_menu()
    if user_input == ("B"):
        magenta_string("Exiting the game...".center(80))
        time.sleep(2)
        clear_terminal()
        exit_game()
    if user_input == ("C"):
        magenta_string("Loading new fact...".center(80))
        time.sleep(2)
        clear_terminal()
        show_fact()


def select_difficulty():
    """ Allows the user to select a difficulty """
    multiple_blank_lines()
    blank_line()
    blank_line()
    blank_line()
    blank_line()
    red_string("Please select a difficulty\n".center(80))
    white_string('A) Easy'.center(80))
    white_string('B) Medium'.center(80))
    white_string('C) Hard'.center(80))
    user_input = input().capitalize()
    if user_input == ("A"):
        magenta_string("Loading easy questions...".center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(easy_question_list)
    elif user_input == ("B"):
        magenta_string("Loading medium questions...".center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(medium_question_list)
    elif user_input == ("C"):
        magenta_string("Loading hard questions...".center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(hard_question_list)
    else:
        magenta_string("Please enter either A, B or C".center(80))
        time.sleep(2)
        clear_terminal()
        select_difficulty()


def show_leaderboards():
    """ Shows the leaderboards to the user """
    leaderboard.sort((2, 'des'))
    print(tabulate(data[0:9], tablefmt='fancy_grid'))
    quick_menu()


def show_game_stats():
    """Shows the game stats"""
    games_played = leaderboard.row_count - 1
    solid_line(new_line_at_end=True)
    white_string(f"Overall games played: {games_played}\n".center(80))
    total_points = []
    for item in leaderboard.col_values(2):
        if item.isdigit():
            total_points.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(f"Overall points accumulated: {sum(total_points)}\n".center(80))
    total_correct = []
    for item in leaderboard.col_values(3):
        if item.isdigit():
            total_correct.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(f"Overall correct questions answered: {sum(total_correct)}\n".center(80))
    total_incorrect = []
    for item in leaderboard.col_values(4):
        if item.isdigit():
            total_incorrect.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(f"Overall incorrect questions answered: {sum(total_incorrect)}\n".center(80))
    solid_line(new_line_at_end=True)
    quick_menu(centered=True)


def clear_terminal():
    """ Clears the terminal """
    os.system('clear')


def exit_game():
    """ Exits the game """
    white_string("Thank you for playing\n")
    white_string("Shutting the program down...\n")
    time.sleep(2)
    green_string("Program shutdown successfully")
    sys.exit()


def show_game_rules():
    """ Displays the game rules to the user """
    white_string("Currently under construction\n")
    quick_menu()


def show_fact():
    """ Displays a random F1 fact to the user """
    multiple_blank_lines()
    blank_line()
    blank_line()
    solid_line(new_line_at_end=True)
    random_fact = get_random_fact()
    print(random_fact.center(80))
    blank_line()
    solid_line(new_line_at_end=False)
    fact_menu()


def get_random_fact():
    """ Stores all facts in a list, picks one at random and returns it as a string"""
    fact_list = []
    for i in fact_data:
        fact_list.append(i)
    load_fact = random.choice(fact_list)
    return ''.join(load_fact)


def submit_feedback():
    """ Allows the user to submit feedback """
    white_string(name + ", please submit your feedback below\n")
    white_string("If you wish to leave this screen before submitting a message, please click the  run program button below\n")
    user_feedback = input("Enter feedback: ")
    blank_line()
    magenta_string("Thank you for your feedback, uploading now...\n")
    time.sleep(2)
    feedback.append_row(values=[name, user_feedback, date])
    green_string("Feedback uploaded successfully!\n")
    quick_menu()


def main_menu():
    """ Displays the main menu to the user that allows them to navigate the application """
    blank_line()
    blank_line()
    blank_line()
    blank_line()
    red_string(f"Welcome to the main menu, {name}\n".center(80))
    red_string("Please select an option from the menu\n".center(80))
    blank_line()
    white_string("(A) Start the quiz".center(80))
    white_string("(B) View the leaderboards".center(80))
    white_string("(C) View game statistics".center(80))
    white_string("(D) View game rules".center(80))
    white_string("(E) View an F1 fact".center(80))
    white_string("(F) Submit feedback".center(80))
    white_string("(G) Exit the game\n".center(80))
    user_input = input("".center(35))
    blank_line()
    while True:
        if user_input not in {"A", "B", "C", "D", "E", "F", "G", "a", "b", "c", "d", "e", "f", "g"}:
            yellow_string("Invalid input! Please enter either A, B, C, D, E, F or G\n")
            time.sleep(1)
            clear_terminal()
            main_menu()
        else:
            break
    if user_input == ("A") or ("a"):
        magenta_string("Great stuff, starting a new quiz now...".center(80))
        time.sleep(2)
        clear_terminal()
        select_difficulty()
    if user_input == ("B") or ("b"):
        magenta_string("Loading the leaderboards...".center(80))
        time.sleep(2)
        clear_terminal()
        show_leaderboards()
    if user_input == ("C") or ("c"):
        magenta_string("Loading the game statistics...".center(80))
        time.sleep(2)
        clear_terminal()
        show_game_stats()
    if user_input == ("D") or ("d"):
        magenta_string("Loading the game rules...".center(80))
        time.sleep(2)
        clear_terminal()
        show_game_rules()
    if user_input == ("E") or ("e"):
        magenta_string("Loading the F1 fact display...".center(80))
        time.sleep(2)
        clear_terminal()
        show_fact()
    if user_input == ("F") or ("f"):
        magenta_string("Loading submit feedback...".center(80))
        time.sleep(2)
        clear_terminal()
        submit_feedback()
    if user_input == ("G") or ("g"):
        magenta_string("Exiting the game...".center(80))
        time.sleep(2)
        clear_terminal()
        exit_game()
print("Loading game files...")
time.sleep(2)
green_string("Game files successfully loaded")
time.sleep(2)
clear_terminal()
multiple_blank_lines()
formula_1_text()
days_to_new_season()
blank_line()
while True:
    white_string("Please enter your name below:\n".center(80))
    name = input("".center(35))
    if len(name) > 7 or name.isspace() or name == "":
        blank_line()
        yellow_string('Please enter a name that is 7 characters or less'.center(80))
    else:
        break
time.sleep(2)
clear_terminal()

main_menu()
