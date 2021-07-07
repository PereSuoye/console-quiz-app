import json
import random

with open("quiz_app_question.json") as f:
    questions = json.load(f)

def play_quiz():
    