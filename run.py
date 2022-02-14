''' Main file to run the F1 app '''


from datetime import datetime
import os
import time
import sys
import random
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from print import cyan_string, formula_1_text, green_string
from print import red_string, white_string, yellow_string, blank_line
from print import solid_line, thank_you, magenta_string, multiple_blank_lines
from questions import easy_question_list
from questions import medium_question_list
from questions import hard_question_list


SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ci_project_portfolio_3')
leaderboard = SHEET.worksheet('leaderboard')
facts = SHEET.worksheet('facts')
feedback = SHEET.worksheet('feedback')
track_info = SHEET.worksheet('track_info')
calendar = SHEET.worksheet('calendar')
drivers = SHEET.worksheet('drivers')
commands = SHEET.worksheet('commands')
nowdate = datetime.now()
date = nowdate.strftime('%d/%m/%Y')


def view_track_list():
    ''' Displays a list of tracks the user can enter '''
    show_commands = commands.get_all_values()
    print(tabulate(show_commands, tablefmt='simple'))
    blank_line()
    white_string(
                'Typing in one of the above commands when on '
                'the select track page will load information '
                'about that track'
                )
    blank_line()
    while True:
        cyan_string('A) Return back to select track\n')
        user_input = input().upper()
        blank_line()
        if user_input not in {'A'}:
            yellow_string('Invalid input! Please try again \n')
            time.sleep(2)
            clear_terminal()
            view_track_list()
        else:
            break
    if user_input == ('A'):
        magenta_string(
                      f'Understood {name}, returning '
                      f'back to select a track...'
                      )
        time.sleep(2)
        clear_terminal()
        select_track()


def track_list_menu():
    ''' A menu for the user so they can view another track '''
    while True:
        cyan_string('A) Return to F1 Info Hub B) Select a new track\n')
        user_input = input().upper()
        blank_line()
        if user_input not in {'A', 'B'}:
            yellow_string('Invalid input! Please enter either A or B\n')
        else:
            break
    if user_input == ('A'):
        magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to the F1 Info Hub...'
                      )
        time.sleep(2)
        clear_terminal()
        f1_info_hub()
    if user_input == ('B'):
        magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to select a track...'
                      )
        time.sleep(2)
        clear_terminal()
        select_track()


def view_calendar():
    ''' Shows the user the current F1 2022 season calendar'''
    clear_terminal()
    show_calendar = calendar.get_all_values()
    print(tabulate(show_calendar, headers='firstrow', tablefmt='simple'))
    blank_line()
    quick_menu(f1_quick_menu=True)


def view_drivers():
    '''
    Shows the user the current F1 2022 drivers
    and some statistics about them
    '''
    clear_terminal()
    show_drivers = drivers.get_all_values()
    print(tabulate(show_drivers, headers='firstrow', tablefmt='simple'))
    blank_line()
    quick_menu(f1_quick_menu=True)


def select_track():
    ''' Used to allow the user to select a track to view info '''
    multiple_blank_lines()
    while True:
        white_string(
                    'Please enter a track name to view '
                    'information about it\n'.center(80)
                    )
        white_string(
                    'For example, you could type '
                    '"silverstone", "jeddah" or "spa"\n'.center(80)
                    )
        white_string(
                    'We recommend you type the below command '
                    'to see what you can enter\n'.center(80)
                    )
        green_string('view list\n'.center(80))
        white_string(
                    'Alternatively you can type the below command to '
                    'return to the F1 Quiz Hub \n'.center(80)
                    )
        red_string('exit\n'.center(80))
        user_input = input(''.center(34)).lower()
        blank_line()
        if user_input not in {
                            'view list', 'exit', 'paul ricard', 'silverstone',
                            'sakhir', 'jeddah', 'albert park', 'imola',
                            'miami gardens', 'barcelona', 'monte carlo',
                            'baku', 'montreal', 'red bull ring',
                            'hungaroring', 'spa', 'zandvoort', 'monza',
                            'sochi', 'marina bay', 'suzuka', 'americas',
                            'autodromo', 'interlagos', 'yas marina'
                             }:
            yellow_string('Invalid input! Please try again \n'.center(80))
            time.sleep(2)
            clear_terminal()
            select_track()
        else:
            break
    if user_input == ('view list'):
        magenta_string(f'Understood {name}, loading the list...'.center(80))
        time.sleep(2)
        clear_terminal()
        view_track_list()
    if user_input == ('exit'):
        magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to the F1 Info Hub...'.center(80)
                      )
        time.sleep(2)
        clear_terminal()
        f1_info_hub()
    if user_input == ('paul ricard'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        paul_ricard = track_info.get_values('A1:B8')
        print(tabulate(paul_ricard, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('silverstone'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        silverstone = track_info.get_values('A10:B17')
        print(tabulate(silverstone, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('sakhir'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        sakhir = track_info.get_values('A19:B26')
        print(tabulate(sakhir, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('jeddah'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        jeddah = track_info.get_values('A28:B35')
        print(tabulate(jeddah, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('albert park'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        albert_park = track_info.get_values('A37:B44')
        print(tabulate(albert_park, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('imola'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        imola = track_info.get_values('A46:B53')
        print(tabulate(imola, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('miami gardens'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        miami_gardens = track_info.get_values('A55:B62')
        print(tabulate(miami_gardens, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('barcelona'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        barcelona = track_info.get_values('A64:B71')
        print(tabulate(barcelona, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('monte carlo'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        monte_carlo = track_info.get_values('A73:B80')
        print(tabulate(monte_carlo, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('baku'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        baku = track_info.get_values('A82:B89')
        print(tabulate(baku, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('montreal'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        montreal = track_info.get_values('A91:B98')
        print(tabulate(montreal, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('red bull ring'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        red_bull_ring = track_info.get_values('A100:B107')
        print(tabulate(red_bull_ring, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('hungaroring'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        hungaroring = track_info.get_values('A109:B116')
        print(tabulate(hungaroring, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('spa'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        spa = track_info.get_values('A118:B125')
        print(tabulate(spa, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('zandvoort'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        zandvoort = track_info.get_values('A127:B134')
        print(tabulate(zandvoort, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('monza'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        monza = track_info.get_values('A136:B143')
        print(tabulate(monza, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('sochi'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        sochi = track_info.get_values('A145:B152')
        print(tabulate(sochi, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('marina bay'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        marina_bay = track_info.get_values('A154:B161')
        print(tabulate(marina_bay, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('suzuka'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        suzuka = track_info.get_values('A163:B170')
        print(tabulate(suzuka, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('americas'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        americas = track_info.get_values('A172:B179')
        print(tabulate(americas, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('autodromo'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        autodromo = track_info.get_values('A181:B188')
        print(tabulate(autodromo, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('interlagos'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        interlagos = track_info.get_values('A190:B197')
        print(tabulate(interlagos, tablefmt='plain'))
        blank_line()
        track_list_menu()
    if user_input == ('yas marina'):
        magenta_string(f'Understood {name}, loading track info...'.center(80))
        time.sleep(2)
        clear_terminal()
        yas_marina = track_info.get_values('A199:B206')
        print(tabulate(yas_marina, tablefmt='plain'))
        blank_line()
        track_list_menu()


def days_to_new_season():
    '''
    Countsdown to the F1 2022 season and
    displays the remaining days to the user
    '''
    futuredate = datetime.strptime('Mar 18 2022  00:00', '%b %d %Y %H:%M')
    count = int((futuredate-nowdate).total_seconds())
    days = count//86400
    number_of_days = '{} days'.format(days)
    if days <= 0:
        return green_string('The F1 2022 season has started!'.center(80))
    return red_string(
                     f'Days left until F1 2022 Season: '
                     f'{number_of_days}'.center(80))


def start_quiz(selected_difficulty):
    ''' Loads the questions and validates the users answer '''
    score = 0
    correct = 0
    incorrect = 0
    questions = random.sample(selected_difficulty, 10)
    for question in questions:
        while True:
            user_answer = input(question.question).upper()
            if user_answer not in {'A', 'B', 'C'}:
                yellow_string(
                             'Invalid input! You can attempt '
                             'the question again\n'
                             )
            else:
                break
        if user_answer == question.answer:
            green_string('Correct answer!\n')
            time.sleep(2)
            correct += 1
            if selected_difficulty == easy_question_list:
                difficulty_selected = 'Easy'
                score += 10
            elif selected_difficulty == medium_question_list:
                difficulty_selected = 'Medium'
                score += 20
            elif selected_difficulty == hard_question_list:
                difficulty_selected = 'Hard'
                score += 40
        else:
            incorrect += 1
            red_string('Incorrect answer\n')
            time.sleep(2)
    white_string(
                f'Great stuff {name}, you have '
                f'managed to answer all the questions!\n')
    white_string(
                f'You chose {difficulty_selected} difficulty and scored '
                f'{score} points, answering {correct} correct and '
                f'{incorrect} incorrect\n'
                )
    time.sleep(2)
    magenta_string('Please wait, adding your score to the leaderboard...\n')
    leaderboard.append_row(values=[name, score, correct,
                           incorrect, difficulty_selected,
                           date])
    time.sleep(2)
    leaderboard.sort((2, 'des'))
    green_string('Leaderboard updated successfully!\n')
    quick_menu()


def quick_menu(centered=False, f1_quick_menu=False):
    '''Small navigation menu for the user'''
    if centered:
        while True:
            cyan_string(
                        'A) Return to Quiz Hub '
                        'B) Return to Main Menu\n'.center(80)
                       )
            user_input = input(''.center(38)).upper()
            blank_line()
            if user_input not in {'A', 'B'}:
                yellow_string('Invalid input! Please enter either A or B\n')
            else:
                break
        if user_input == ('A'):
            magenta_string(
                          f'Understood {name}, redirecting '
                          f'back to the Quiz Hub...'.center(80)
                          )
            time.sleep(2)
            clear_terminal()
            quiz_hub()
        if user_input == ('B'):
            magenta_string(
                           f'Understood {name}, redirecting '
                           f'back to the Main Menu...'.center(80)
                          )
            time.sleep(2)
            clear_terminal()
            main_menu()
    if f1_quick_menu:
        while True:
            cyan_string('A) Return to F1 Info Hub B) Return to Main Menu\n')
            user_input = input().upper()
            blank_line()
            if user_input not in {'A', 'B'}:
                yellow_string('Invalid input! Please enter either A or B\n')
            else:
                break
        if user_input == ('A'):
            magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to the F1 Info Hub...'
                      )
            time.sleep(2)
            clear_terminal()
            f1_info_hub()
        if user_input == ('B'):
            magenta_string(
                          f'Understood {name}, redirecting '
                          f'back to the Main Menu...'
                          )
            time.sleep(2)
            clear_terminal()
            main_menu()
    else:
        while True:
            cyan_string('A) Return to Quiz Hub B) Return to Main Menu\n')
            user_input = input().upper()
            blank_line()
            if user_input not in {'A', 'B'}:
                yellow_string('Invalid input! Please enter either A or B\n')
            else:
                break
        if user_input == ('A'):
            magenta_string(
                          f'Understood {name}, redirecting '
                          f'back to the Quiz Hub...'
                          )
            time.sleep(2)
            clear_terminal()
            quiz_hub()
        if user_input == ('B'):
            magenta_string(
                          f'Understood {name}, redirecting '
                          f'back to the Main Menu...'
                          )
            time.sleep(2)
            clear_terminal()
            main_menu()


def fact_menu():
    '''Small navigation menu for the user'''
    while True:
        cyan_string(
            'A) Return to F1 Info Hub '
            'B) Return to Main Menu '
            'C) Load new fact\n'.center(80))
        user_input = input(''.center(38)).upper()
        blank_line()
        if user_input not in {'A', 'B', 'C'}:
            yellow_string(
                         'Invalid input! Please enter either '
                         'A, B, or C \n'.center(80)
                         )
        else:
            break
    if user_input == ('A'):
        magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to the F1 Info Hub...'.center(80)
                      )
        time.sleep(2)
        clear_terminal()
        f1_info_hub()
    if user_input == ('B'):
        magenta_string(
                      f'Understood {name}, redirecting '
                      f'back to the Main Menu...'.center(80))
        time.sleep(2)
        clear_terminal()
        main_menu()
    if user_input == ('C'):
        magenta_string('Loading new fact...'.center(80))
        time.sleep(2)
        clear_terminal()
        show_fact()


def select_difficulty():
    ''' Allows the user to select a difficulty '''
    multiple_blank_lines()
    blank_line()
    blank_line()
    blank_line()
    red_string('Please select a difficulty\n'.center(80))
    white_string('A) Easy'.center(80))
    white_string('B) Medium'.center(80))
    white_string('C) Hard\n'.center(80))
    user_input = input(''.center(38)).upper()
    blank_line()
    if user_input == ('A'):
        magenta_string('Loading easy questions...'.center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(easy_question_list)
    elif user_input == ('B'):
        magenta_string('Loading medium questions...'.center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(medium_question_list)
    elif user_input == ('C'):
        magenta_string('Loading hard questions...'.center(80))
        time.sleep(2)
        clear_terminal()
        start_quiz(hard_question_list)
    else:
        magenta_string('Please enter either A, B or C'.center(80))
        time.sleep(2)
        clear_terminal()
        select_difficulty()


def show_leaderboards():
    ''' Shows the leaderboards to the user '''
    leaderboard = SHEET.worksheet('leaderboard')
    leaderboard.sort((2, 'des'))
    data = leaderboard.get_all_values()
    print(tabulate(data[0:9], tablefmt='fancy_grid'))
    quick_menu()


def show_quiz_stats():
    '''Shows the game stats'''
    games_played = leaderboard.row_count - 1
    solid_line(new_line_at_end=True)
    white_string(f'Overall games played: {games_played}\n'.center(80))
    total_points = []
    for item in leaderboard.col_values(2):
        if item.isdigit():
            total_points.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(
                f'Overall points accumulated: '
                f'{sum(total_points)}\n'.center(80)
                )
    total_correct = []
    for item in leaderboard.col_values(3):
        if item.isdigit():
            total_correct.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(
                f'Overall correct questions answered: '
                f'{sum(total_correct)}\n'.center(80)
                )
    total_incorrect = []
    for item in leaderboard.col_values(4):
        if item.isdigit():
            total_incorrect.append(int(item))
    solid_line(new_line_at_end=True)
    white_string(
                f'Overall incorrect questions answered: '
                f'{sum(total_incorrect)}\n'.center(80)
                )
    solid_line(new_line_at_end=True)
    quick_menu(centered=True)


def clear_terminal():
    ''' Clears the terminal '''
    # os.system('clear')
    os.system("printf '\ec'")


def exit_app():
    ''' Exits the app '''
    blank_line()
    blank_line()
    blank_line()
    blank_line()
    white_string(f'Thank you very much for stopping by, {name}\n'.center(80))
    white_string('We hope you enjoyed your time on the application'.center(80))
    white_string('and we hope to see you back shortly!\n'.center(80))
    thank_you()
    time.sleep(2)
    magenta_string('Shutting the application down...\n'.center(80))
    time.sleep(2)
    green_string('Application shutdown successfully\n'.center(80))
    white_string(
                'Click the RUN APP button if you '
                'wish to restart the app'.center(80)
                )
    sys.exit()


def show_quiz_rules():
    ''' Displays the quiz rules to the user '''
    white_string(
                'The quiz has 3 different difficulty '
                'levels to choose from\n'
                )
    white_string(
                'Selecting Easy will result in 10 points '
                'per correct question\n'
                )
    white_string(
                'Selecting Medium will result in 20 points '
                'per correct question\n'
                )
    white_string(
                'Selecting Hard will result in 40 points '
                'per correct question\n'
                )
    white_string(
                'There is no time limit, so you can '
                'take your time on each question\n'
                )
    white_string(
                'The questions are all general knowledge '
                'questions and the answers are in the form '
                'of multiple choice\n'
                )
    white_string(
                'Upon completion, your score will be '
                'automatically uploaded to the hiscores\n'
                )
    quick_menu()


def show_fact():
    ''' Displays a random F1 fact to the user '''
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
    '''
    Stores all facts in a list, picks one
    at random and returns it as a string
    '''
    fact_data = facts.get_all_values()
    fact_list = []
    for i in fact_data:
        fact_list.append(i)
    load_fact = random.choice(fact_list)
    return ''.join(load_fact)


def submit_feedback():
    ''' Allows the user to submit feedback '''
    white_string(f'{name}, please submit your feedback below\n')
    white_string(
                'If you wish to leave this screen before '
                'submitting a message, please click the  '
                'run app button below\n')
    user_feedback = input('Enter feedback: ')
    blank_line()
    magenta_string('Thank you for your feedback, uploading now...\n')
    time.sleep(2)
    feedback.append_row(values=[name, user_feedback, date])
    green_string('Feedback uploaded successfully!\n')
    time.sleep(1)
    white_string('Returning back to the main menu, please wait')
    time.sleep(3)
    clear_terminal()
    main_menu()


def quiz_hub():
    ''' Displays the main menu for the quiz menu options '''
    multiple_blank_lines()
    red_string(f'Welcome to the Quiz Hub, {name}\n'.center(80))
    red_string('Please select an option from the menu\n'.center(80))
    blank_line()
    white_string('(A) Start the quiz'.center(80))
    white_string('(B) View the leaderboards'.center(80))
    white_string('(C) View quiz statistics'.center(80))
    white_string('(D) View quiz rules'.center(80))
    white_string('(E) Return back to the main menu\n'.center(80))
    user_input = input(''.center(38)).upper()
    blank_line()
    while True:
        if user_input not in {'A', 'B', 'C', 'D', 'E'}:
            yellow_string(
                         'Invalid input! Please enter either '
                         'A, B, C, D or E\n'.center(80))
            time.sleep(1)
            clear_terminal()
            quiz_hub()
        else:
            break
    if user_input == ('A'):
        magenta_string('Great stuff, starting a new quiz now...'.center(80))
        time.sleep(2)
        clear_terminal()
        select_difficulty()
    if user_input == ('B'):
        magenta_string('Loading the leaderboards...'.center(80))
        leaderboard.sort((2, 'des'))
        time.sleep(2)
        clear_terminal()
        show_leaderboards()
    if user_input == ('C'):
        magenta_string('Loading the quiz statistics...'.center(80))
        time.sleep(2)
        clear_terminal()
        show_quiz_stats()
    if user_input == ('D'):
        magenta_string('Loading the quiz rules...'.center(80))
        time.sleep(2)
        clear_terminal()
        show_quiz_rules()
    if user_input == ('E'):
        magenta_string('Returning back to the main menu...'.center(80))
        time.sleep(2)
        clear_terminal()
        main_menu()


def f1_info_hub():
    ''' Displays the main menu for the F1 info hub '''
    multiple_blank_lines()
    red_string(f'Welcome to the F1 Info Hub, {name}\n'.center(80))
    red_string('Please select an option from the menu\n'.center(80))
    blank_line()
    white_string('(A) View an F1 fact'.center(80))
    white_string('(B) View select track menu'.center(80))
    white_string('(C) View F1 2022 calendar'.center(80))
    white_string('(D) View F1 2022 drivers'.center(80))
    white_string('(E) Return back to the main menu\n'.center(80))
    user_input = input(''.center(38)).upper()
    blank_line()
    while True:
        if user_input not in {'A', 'B', 'C', 'D', 'E'}:
            yellow_string(
                         'Invalid input! Please enter either '
                         'A, B, C, D or E\n'.center(80)
                         )
            time.sleep(1)
            clear_terminal()
            f1_info_hub()
        else:
            break
    if user_input == ('A'):
        magenta_string('Loading the F1 fact display...'.center(80))
        time.sleep(2)
        clear_terminal()
        show_fact()
    if user_input == ('B'):
        magenta_string('Loading select track..'.center(80))
        time.sleep(2)
        clear_terminal()
        select_track()
    if user_input == ('C'):
        magenta_string('Loading 2022 calendar..'.center(80))
        time.sleep(2)
        clear_terminal()
        view_calendar()
    if user_input == ('D'):
        magenta_string('Loading current F1 drivers..'.center(80))
        drivers.sort((5, 'des'))
        time.sleep(2)
        clear_terminal()
        view_drivers()
    if user_input == ('E'):
        magenta_string('Returning back to the main menu...'.center(80))
        time.sleep(2)
        clear_terminal()
        main_menu()


def main_menu():
    '''
    Displays the main menu to the user that
    allows them to navigate the application
    '''
    multiple_blank_lines()
    red_string(f'Welcome to the Main Menu, {name}\n'.center(80))
    red_string('Please select an option from the menu\n'.center(80))
    blank_line()
    white_string('(A) View Quiz Hub'.center(80))
    white_string('(B) View F1 Info Hub'.center(80))
    white_string('(C) Submit feedback'.center(80))
    white_string('(D) Exit the app\n'.center(80))
    user_input = input(''.center(38)).upper()
    blank_line()
    while True:
        if user_input not in {'A', 'B', 'C', 'D'}:
            yellow_string(
                         'Invalid input! Please enter either '
                         'A, B, C, D or E\n'.center(80)
                         )
            time.sleep(1)
            clear_terminal()
            main_menu()
        else:
            break
    if user_input == ('A'):
        magenta_string('Loading the Quiz Hub...'.center(80))
        time.sleep(2)
        clear_terminal()
        quiz_hub()
    if user_input == ('B'):
        magenta_string('Loading the F1 Info Hub'.center(80))
        time.sleep(2)
        clear_terminal()
        f1_info_hub()
    if user_input == ('C'):
        magenta_string('Loading submit feedback...'.center(80))
        time.sleep(2)
        clear_terminal()
        submit_feedback()
    if user_input == ('D'):
        magenta_string('Exiting the application...'.center(80))
        time.sleep(2)
        clear_terminal()
        exit_app()

clear_terminal()
multiple_blank_lines()
formula_1_text()
days_to_new_season()
blank_line()
while True:
    white_string('Please enter your name below:\n'.center(80))
    name = input(''.center(35))
    if len(name) > 14 or name.isspace() or name == '':
        blank_line()
        yellow_string(
                     'Please enter a name that is '
                     '14 characters or less'.center(80)
                     )
    else:
        break
time.sleep(2)
leaderboard.sort((2, 'des'))
clear_terminal()
main_menu()
