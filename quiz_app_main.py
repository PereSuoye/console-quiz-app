import json
import random

with open("quiz_app_question.json") as f:
   questions = json.load(f)

def play_quiz():
    
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_)
]