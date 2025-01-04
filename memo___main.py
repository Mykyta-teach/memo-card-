from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication


app = QApplication([])

from memo___app import *
from memo___card_layout import *


class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Яблуко" , "apple", "catterpillar", "application", "bulding")
q2 = Question("q1", "a", "w1", "w2", "w3")
#q3= Question("")
#q4 = Question("")


radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]

questions = [q1, q2,]

def new_questions():
    global current_question
    current_question = choice(questions)
    lb_question.setText(current_question.question)
    lb_right_answer.setText(current_question.answer)

    shuffle(radio_buttons)

    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)


new_questions()

def check_result():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                current_question.got_right()
                lb_result.setText("Вірно!")
                answer.setChecked(False)
                break
            else:
                current_question.got_wrong()
                lb_result.setText("Не вірно!")
    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() != "Наступне питання":
        check_result()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText("Наступне питання")
    else:
        new_questions()
        
        gb_question.show()
        gb_answer.hide()
        
        btn_next.setText("Відповідь")

btn_next.clicked.connect(click_ok)


window.show()
app.exec_()