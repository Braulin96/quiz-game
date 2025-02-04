from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#first_approach
# questions_list = []
# i = 0
#
# for i in range (0, len(question_data)):
#     questions = Question (question_data[i]["text"], question_data[i]["answer"])
#     questions_list.append(questions)
#
# print (questions_list[0].text)
#

questions_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print (f"Your final score was {quiz.score}/{len(quiz.question_list)}")
