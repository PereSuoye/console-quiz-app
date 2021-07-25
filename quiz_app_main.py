import json
import random


with open("questions.json") as f:
   questions = json.load(f)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

]
def play_quiz(questions_prompts):
    score = 0
    for question in questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1
    print(f"You got {str(score)} / {str(len(questions))} correct.")

print(questions)

