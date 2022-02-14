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
     "\u001b[36;1mWhat is the nickname of Ferrari?\u001b[0m\n \
     (A) The Prancing Horse\n \
     (B) The Dancing Horse\n \
     (C) The Laughing Horse\n",

     "\u001b[36;1mWhich driver won the first ever F1 world "
     "championship title?\u001b[0m\n \
     (A) Niki Lauda\n \
     (B) Giuseppe Farina\n \
     (C) Michael Schumacher\n",

     "\u001b[36;1mWho is the only woman to get points in an "
     "F1 World Championship race?\u001b[0m\n \
     (A) Divina Galica\n \
     (B) Desire Wilson\n \
     (C) Lella Lombardi\n",

     "\u001b[36;1mIf a few drivers set identical lap times, "
     "then who would get the priority?\u001b[0m\n \
     (A) The driver who set first\n \
     (B) The driver who set last\n \
     (C) None of them\n",

     "\u001b[36;1mHow old was Ayrton Senna when he died?\u001b[0m\n \
     (A) 37 years\n \
     (B) 34 years\n \
     (C) 30 years\n",

     "\u001b[36;1mWhich movie was made about Niki Lauda's "
     "racing career?\u001b[0m\n \
     (A) Blast\n \
     (B) Race\n \
     (C) Rush\n",

     "\u001b[36;1mJenson Button won the 2009 Formula One "
     "World Championship driving for which team?\u001b[0m\n \
     (A) Brawn GP\n \
     (B) McLaren\n \
     (C) Renault\n",

     "\u001b[36;1mWho was the first ever British Formula "
     "One World Champion?\u001b[0m\n \
     (A) Lewis Hamilton\n \
     (B) Mike Hawthorne\n \
     (C) Niki Lauda\n",

     "\u001b[36;1mSebastian Vettel won the championship in "
     "2010, 2011, 2012 and 2013, with which racing team?\u001b[0m\n \
     (A) Ferrari\n \
     (B) McLaren\n \
     (C) Red Bull\n",

     "\u001b[36;1mWhich car team were Constructors' Champions "
     "in 2017?\u001b[0m\n \
     (A) Mercedes\n \
     (B) McLaren\n \
     (C) Haas\n",

     "\u001b[36;1mIn which year was the World Drivers' Championship "
     "first awarded?\u001b[0m\n \
     (A) 1960\n \
     (B) 1950\n \
     (C) 1940\n",

     "\u001b[36;1mIn which year did Lewis Hamilton win his first "
     "World Championship?\u001b[0m\n \
     (A) 2005\n \
     (B) 2010\n \
     (C) 2008\n",

     "\u001b[36;1mWhat was the previous name of Alpha Tauri?\u001b[0m\n \
     (A) Toro Rosso\n \
     (B) Toro Bosso\n \
     (C) Toro Losso\n",

     "\u001b[36;1mWho is the only driver to beat both Hamilton "
     "and Schumacher as a team-mate?\u001b[0m\n \
     (A) Jenson Button\n \
     (B) Nico Rosberg\n \
     (C) Valtteri Bottas\n",

     "\u001b[36;1mWho was the first Mexican driver to get a "
     "podium in Mexico?\u001b[0m\n \
     (A) Pedro Rodríguez\n \
     (B) Moisés Solana\n \
     (C) Sergio Perez\n",

     "\u001b[36;1mWhich circuit saw the first F1 Sprint Race trial?\u001b[0m\n \
     (A) Silverstone\n \
     (B) Sochi\n \
     (C) Monza\n",

     "\u001b[36;1mWhich circuit did Pierre Gasly take his first win at?\u001b[0m\n \
     (A) Spa\n \
     (B) Monza\n \
     (C) Jeddah\n",

     "\u001b[36;1mHow many World Championships did Ayrton Senna win?\u001b[0m\n \
     (A) 1\n \
     (B) 2\n \
     (C) 3\n",

     "\u001b[36;1mAt which track did Daniel Ricciardo win his first "
     "race for McLaren?\u001b[0m\n \
     (A) Monza\n \
     (B) Paul Ricard\n \
     (C) Baku\n",

     "\u001b[36;1mWhen was the halo first used in F1?\u001b[0m\n \
     (A) 2015\n \
     (B) 2018\n \
     (C) 2020\n",
]

medium_question_list = [
    Question(medium_questions[0], "A"),
    Question(medium_questions[1], "B"),
    Question(medium_questions[2], "C"),
    Question(medium_questions[3], "A"),
    Question(medium_questions[4], "B"),
    Question(medium_questions[5], "C"),
    Question(medium_questions[6], "A"),
    Question(medium_questions[7], "B"),
    Question(medium_questions[8], "C"),
    Question(medium_questions[9], "A"),
    Question(medium_questions[10], "B"),
    Question(medium_questions[11], "C"),
    Question(medium_questions[12], "A"),
    Question(medium_questions[13], "B"),
    Question(medium_questions[14], "C"),
    Question(medium_questions[15], "A"),
    Question(medium_questions[16], "B"),
    Question(medium_questions[17], "C"),
    Question(medium_questions[18], "A"),
    Question(medium_questions[19], "B"),
]

hard_questions = [
     "\u001b[36;1mThe title “Grand Prix” was first used for "
     "a motor race in which country?\u001b[0m\n \
     (A) France\n \
     (B) Britian\n \
     (C) Spain\n",

     "\u001b[36;1mJuan Manuel Fangio, one of the greatest F1 "
     "drivers, took his last world championship title in which year?\u001b[0m\n \
     (A) 1952\n \
     (B) 1957\n \
     (C) 1962\n",

     "\u001b[36;1mFord provided engines to F1 for many years before forming "
     "its own team in 2000 under the name of which subsidiary marques?\u001b[0m\n \
     (A) McLaren\n \
     (B) Brawn GP\n \
     (C) Jaguar\n",

     "\u001b[36;1mFor what country did Emerson Fittipaldi and "
     "Wilson Fittipaldi compete and win two world titles?\u001b[0m\n \
     (A) Brazil\n \
     (B) Columbia\n \
     (C) Mexico\n",

     "\u001b[36;1mWhich circuit held the first race of the French Grand Prix "
     "in 1950?\u001b[0m\n \
     (A) Paul Ricard\n \
     (B) Reims\n \
     (C) Le Mans\n",

     "\u001b[36;1mWhich major car manufacturer was successful at "
     "supplying engines for McLaren between 1988 and 1992, but "
     "failed when the two renewed their cooperation in 2015?\u001b[0m\n \
     (A) Ford\n \
     (B) Mercedes\n \
     (C) Honda\n",

     "\u001b[36;1mThe Hungarian Grand Prix became a part of the F1 world "
     "championship during which decade?\u001b[0m\n \
     (A) 1980s\n \
     (B) 1970s\n \
     (C) 1960s\n",

     "\u001b[36;1mHSBC was the title sponsor for which F1 team from 1997 "
     "to 1999?\u001b[0m\n \
     (A) Brawn GP\n \
     (B) Stewart\n \
     (C) Williams\n",

     "\u001b[36;1mHow many Grand Prix's did the Jordan F1 team win between "
     "1995 and 2005?\u001b[0m\n \
     (A) 2\n \
     (B) 1\n \
     (C) 4\n",

     "\u001b[36;1mWhich team won the first World Constructors' "
     "Championship?\u001b[0m\n \
     (A) Vanwall\n \
     (B) Vauxhall\n \
     (C) Volvo\n",

     "\u001b[36;1mWhich circuit hosted the first World "
     "Championship race?\u001b[0m\n \
     (A) Imola\n \
     (B) Silverstone\n \
     (C) Yas Marina\n",

     "\u001b[36;1mWhich race in 2005 saw just 6 cars start?\u001b[0m\n \
     (A) French Grand Prix\n \
     (B) Mexican Grand Prix\n \
     (C) United States Grand Prix\n",

     "\u001b[36;1mWho won the 2008 Canadian Grand Prix?\u001b[0m\n \
     (A) Robert Kubica\n \
     (B) Lewis Hamilton\n \
     (C) Nico Rosberg\n",

     "\u001b[36;1mIn which country did Lewis Hamilton take "
     "his first win?\u001b[0m\n \
     (A) Great Britain\n \
     (B) Canada\n \
     (C) Spain\n",

     "\u001b[36;1mIn which country did Max Verstappen take "
     "his first win?\u001b[0m\n \
     (A) France\n \
     (B) Netherlands\n \
     (C) Spain\n",

     "\u001b[36;1mWhat was the previous name of the Red Bull team?\u001b[0m\n \
     (A) Jaguar\n \
     (B) Ford\n \
     (C) Vauxhall\n",

     "\u001b[36;1mAt which circuit did three drivers set identical pole "
     "position times in 1997?\u001b[0m\n \
     (A) Silverstone\n \
     (B) Jerez\n \
     (C) Imola\n",

     "\u001b[36;1mWhat team did Fernando Alonso win his first 2 "
     "championships with?\u001b[0m\n \
     (A) McLaren\n \
     (B) Ferrari\n \
     (C) Renault\n",

     "\u001b[36;1mWhat country is Juan Pablo Montoya from?\u001b[0m\n \
     (A) Colombia\n \
     (B) Mexico\n \
     (C) Argentina\n",

     "\u001b[36;1mWho was the first Finnish F1 World Champion?\u001b[0m\n \
     (A) Valtteri Bottas\n \
     (B) Keke Rosberg\n \
     (C) Kimi Räikkönen\n",

]

hard_question_list = [
    Question(hard_questions[0], "A"),
    Question(hard_questions[1], "B"),
    Question(hard_questions[2], "C"),
    Question(hard_questions[3], "A"),
    Question(hard_questions[4], "B"),
    Question(hard_questions[5], "C"),
    Question(hard_questions[6], "A"),
    Question(hard_questions[7], "B"),
    Question(hard_questions[8], "C"),
    Question(hard_questions[9], "A"),
    Question(hard_questions[10], "B"),
    Question(hard_questions[11], "C"),
    Question(hard_questions[12], "A"),
    Question(hard_questions[13], "B"),
    Question(hard_questions[14], "C"),
    Question(hard_questions[15], "A"),
    Question(hard_questions[16], "B"),
    Question(hard_questions[17], "C"),
    Question(hard_questions[18], "A"),
    Question(hard_questions[19], "B"),
]
