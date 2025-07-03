








































# 1:make API for questions
# 2:unscape the html text
# 3:create ui
# 4: create get_next_question(self) methode


# 001 The-Open-Trivia-Database
# https://opentdb.com/
#
# 002 Documentation-on-HTML-Entities
# https://www.w3schools.com/html/html_entities.asp
#
# 003 FreeFormatter-HTML-Unescape-Tool
# https://www.freeformatter.com/html-escape.html
#
# 004 StackOverflow-Answer-on-Unescaping-HTML-Entities-in-Python
# https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string













from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
