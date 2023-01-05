import json
from domain.quiz import Quiz

with open('tests/quiz1.json') as file:
    data = json.loads(file.read())

print(data["name"])

q = Quiz(data)
q.perform()
