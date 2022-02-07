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
        print("Test 12345")
    if user_input == ("B"):
        print("Exiting the game...")
        time.sleep(2)

print("Welcome to the F1 quiz!")
name = input("Please enter your name: ")

main_menu()
