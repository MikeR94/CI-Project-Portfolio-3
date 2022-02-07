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