from question_model import question_model
from data import question_data
from quiz_brain import QuizBrain
from logo import start, end
question_bank = []
for questions in question_data:
    q_text = questions["text"]
    q_answer = questions["answer"]
    n_question = question_model(q_text, q_answer)

    question_bank.append(n_question)\

quiz = QuizBrain(question_bank)
print(start)
while quiz.still_has_questions():
    quiz.next_question()

print("You've successfully completed the quiz!")
print(f"And, Your final score is: {quiz.score}/{quiz.question_num} ")
print(end)