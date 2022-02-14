""" File to store the questions for the quiz """


class Question:
    """
    Questions instance, gets the question
    and the answer
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

easy_questions = [
     '\u001b[36;1mLewis Hamilton won the first F1 world championship '
     'title when he raced for which team?\u001b[0m\n \
     (A) McLaren\n \
     (B) Ferrari\n \
     (C) Mercedes\n',

     "\u001b[36;1mWhat does a red flag mean in the race?\u001b[0m\n \
     (A) Lapped cars must give way to the leaders\n \
     (B) The race is stopped\n \
     (C) Drivers are on the final lap\n",

     "\u001b[36;1mWho is the youngest F1 driver to win a race?\u001b[0m\n \
     (A) Lewis Hamilton\n \
     (B) George Russell\n \
     (C) Max Verstappen\n",

     '\u001b[36;1mHow many driver world titles '
     'did Michael Schumacher win?\u001b[0m\n \
     (A) 7\n \
     (B) 8\n \
     (C) 6\n',

     "\u001b[36;1mHow many points are awarded to "
     "the race winner of each Grand Prix?\u001b[0m\n \
     (A) 30\n \
     (B) 25\n \
     (C) 20\n",

     "\u001b[36;1mWhat are F1 races known as?\u001b[0m\n \
     (A) Grand Canyon\n \
     (B) Grand Finale\n \
     (C) Grand Prix\n",

     "\u001b[36;1mWho is the son of Michael Schumacher?\u001b[0m\n \
     (A) Mick Schumacher\n \
     (B) Tom Schumacher\n \
     (C) James Schumacher\n",

     "\u001b[36;1mHow many gears does a 2022 F1 car have?\u001b[0m\n \
     (A) 7\n \
     (B) 8\n \
     (C) 6\n",

     "\u001b[36;1mWho is the son of Graham Hill?\u001b[0m\n \
     (A) Jack Hill\n \
     (B) Bob Hill\n \
     (C) Damon Hill\n",

     "\u001b[36;1mWho became Mercedes team principal in 2013?\u001b[0m\n \
     (A) Toto Wolff\n \
     (B) Christian Horner\n \
     (C) Guenther Steiner\n",

     "\u001b[36;1mWho was the first driver to reach 100 wins?\u001b[0m\n \
     (A) Max Verstappen\n \
     (B) Lewis Hamilton\n \
     (C) Lando Norris\n",

     "\u001b[36;1mWho is the commentator that is known for saying "
     "'It's lights out and away we go!'\u001b[0m\n \
     (A) Martin Brundle\n \
     (B) Ted Kravitz\n \
     (C) David Croft\n",

     "\u001b[36;1mWho won the 2021 drivers championship in a "
     "controversial final lap at Abu Dhabi?\u001b[0m\n \
     (A) Max Verstappen\n \
     (B) Lewis Hamilton\n \
     (C) Nicholas Latifi\n",

     "\u001b[36;1mHow many driver world titles has Lewis "
     "Hamilton won?\u001b[0m\n \
     (A) 5\n \
     (B) 7\n \
     (C) 6\n",

     "\u001b[36;1mThe driver that qualifies first for the grand "
     "prix is known to be in what position?\u001b[0m\n \
     (A) Pole person\n \
     (B) Pole driver\n \
     (C) Pole position\n",

     "\u001b[36;1mMany F1 drivers begin their careers driving what?\u001b[0m\n \
     (A) Go karts\n \
     (B) Horses\n \
     (C) Dodgems\n",

     "\u001b[36;1mFormula 1 is what kind of sport?\u001b[0m\n \
     (A) Football\n \
     (B) Racing\n \
     (C) Boxing\n",

     "\u001b[36;1mWhat is the main colour for the team Ferrari?\u001b[0m\n \
     (A) Blue\n \
     (B) Green\n \
     (C) Red\n",

     "\u001b[36;1mWhat type of compound is the tyre "
     "with the yellow stripe?\u001b[0m\n \
     (A) Medium\n \
     (B) Hard\n \
     (C) Soft\n",

     "\u001b[36;1mWhat type of compound is the tyre "
     "with the blue stripe?\u001b[0m\n \
     (A) Intermediate\n \
     (B) Wet\n \
     (C) Soft\n",
]

easy_question_list = [
    Question(easy_questions[0], "A"),
    Question(easy_questions[1], "B"),
    Question(easy_questions[2], "C"),
    Question(easy_questions[3], "A"),
    Question(easy_questions[4], "B"),
    Question(easy_questions[5], "C"),
    Question(easy_questions[6], "A"),
    Question(easy_questions[7], "B"),
    Question(easy_questions[8], "C"),
    Question(easy_questions[9], "A"),
    Question(easy_questions[10], "B"),
    Question(easy_questions[11], "C"),
    Question(easy_questions[12], "A"),
    Question(easy_questions[13], "B"),
    Question(easy_questions[14], "C"),
    Question(easy_questions[15], "A"),
    Question(easy_questions[16], "B"),
    Question(easy_questions[17], "C"),
    Question(easy_questions[18], "A"),
    Question(easy_questions[19], "B"),
]

medium_questions = [
     "Medium F1 Question 1\n \
     (A) Medium answer 1\n \
     (B) Medium answer 2\n \
     (C) Medium answer 3\n",

     "Medium F1 Question 2\n \
     (A) Medium answer 1\n \
     (B) Medium answer 2\n \
     (C) Medium answer 3\n",

     "Medium F1 Question 3\n \
     (A) Medium answer 1\n \
     (B) Medium answer 2\n \
     (C) Medium answer 3\n",

     "Medium F1 Question 4\n \
     (A) Medium answer 1\n \
     (B) Medium answer 2\n \
     (C) Medium answer 3\n",

     "Medium F1 Question 5\n \
     (A) Medium answer 1\n \
     (B) Medium answer 2\n \
     (C) Medium answer 3\n",
]

medium_question_list = [
    Question(medium_questions[0], "A"),
    Question(medium_questions[1], "A"),
    Question(medium_questions[2], "A"),
    Question(medium_questions[3], "A"),
    Question(medium_questions[4], "A"),
]

hard_questions = [
     "Hard F1 Question 1\n \
     (A) Hard answer 1\n \
     (B) Hard answer 2\n \
     (C) Hard answer 3\n",

     "Hard F1 Question 2\n \
     (A) Hard answer 1\n \
     (B) Hard answer 2\n \
     (C) Hard answer 3\n",

     "Hard F1 Question 3\n \
     (A) Hard answer 1\n \
     (B) Hard answer 2\n \
     (C) Hard answer 3\n",

     "Hard F1 Question 4\n \
     (A) Hard answer 1\n \
     (B) Hard answer 2\n \
     (C) Hard answer 3\n",

     "Hard F1 Question 5\n \
     (A) Hard answer 1\n \
     (B) Hard answer 2\n \
     (C) Hard answer 3\n",
]

hard_question_list = [
    Question(hard_questions[0], "A"),
    Question(hard_questions[1], "A"),
    Question(hard_questions[2], "A"),
    Question(hard_questions[3], "A"),
    Question(hard_questions[4], "A"),
]
