import os
import time
import gspread
from google.oauth2.service_account import Credentials

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

class Question:
    """
    Questions instance, gets the question
    and the answer
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
     "Easy F1 Question 1\n \
     (A) Easy answer 1\n \
     (B) Easy answer 2\n \
     (C) Easy answer 3\n",

     "Easy F1 Question 2\n \
     (A) Easy answer 1\n \
     (B) Easy answer 2\n \
     (C) Easy answer 3\n",

     "Easy F1 Question 3\n \
     (A) Easy answer 1\n \
     (B) Easy answer 2\n \
     (C) Easy answer 3\n",

     "Easy F1 Question 4\n \
     (A) Easy answer 1\n \
     (B) Easy answer 2\n \
     (C) Easy answer 3\n",

     "Easy F1 Question 5\n \
     (A) Easy answer 1\n \
     (B) Easy answer 2\n \
     (C) Easy answer 3\n",
]

question_list = [
    Question(questions[0], "A"),
    Question(questions[1], "A"),
    Question(questions[2], "A"),
    Question(questions[3], "A"),
    Question(questions[4], "A"),
]

def start_quiz():
    """ Loads the questions and validates the users answer"""
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
    """ Clears the terminal"""
    os.system('clear')


def main_menu():
    """ Displays the main menu to the user that allows them to navigate the application"""
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

print("Welcome to the F1 quiz!")
name = input("Please enter your name: ")

main_menu()
