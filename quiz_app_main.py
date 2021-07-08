import json
import random


questions_prompts = ["What year did Nigeria get independence?\n(a)1959\n(b)1960\n(c)1961\n(d)1962", 
"How many primary colours are there?\n(a)1\n(b)2\n(c)3\n(d)4", 
"What colour are Strawberries?\n(a)yellow\n(b)red\n(c)blue\n(d)green",]

file_name = "quiz_app_question.json"

with open(file_name, "w") as f:
   json.dump(questions_prompts, f)

with open(file_name) as f:
    questions = json.load(f)
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_and_answers = [
    Question(questions[0], "b"),
    Question(questions[1], "c"),
    Question(questions[2], "b"),
]
def play_quiz(questions):
    score = 0
    for question in questions:
        answer = input(str(questions.prompt))
        if answer == questions.answer:
            score += 1
    print(f"You got {str(score)} / {str(len(questions))} correct.")

play_quiz(questions)