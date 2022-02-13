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
     "Lewis Hamilton won the first F1 world championship title when he raced for which team?\n \
     (A) McLaren\n \
     (B) Ferrari\n \
     (C) Mercedes\n",

     "What does a red flag mean in the race?\n \
     (A) Lapped cars must give way to the leaders\n \
     (B) The race is stopped\n \
     (C) Drivers are on the final lap\n",

     "Who is the youngest F1 driver to win a race?\n \
     (A) Lewis Hamilton\n \
     (B) George Russell\n \
     (C) Max Verstappen\n",

     "How many driver world titles did Michael Schumacher win?\n \
     (A) 7\n \
     (B) 8\n \
     (C) 6\n",

     "How many points are awarded to the race winner of each Grand Prix?\n \
     (A) 30\n \
     (B) 25\n \
     (C) 20\n",

     "What are F1 races known as?\n \
     (A) Grand Canyon\n \
     (B) Grand Finale\n \
     (C) Grand Prix\n",
]

easy_question_list = [
    Question(easy_questions[0], "A"),
    Question(easy_questions[1], "B"),
    Question(easy_questions[2], "C"),
    Question(easy_questions[3], "A"),
    Question(easy_questions[4], "B"),
    Question(easy_questions[5], "C"),
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
