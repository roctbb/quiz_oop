import json
from domain.quiz import Quiz

with open('tests/quiz1.json') as file:
    data = json.loads(file.read())

q = Quiz(data)
q.perform()
