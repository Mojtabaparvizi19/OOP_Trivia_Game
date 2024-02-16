import requests
import json
from quiz import Quiz, Question
from UI import QuizInterface


try:
    with open('data.json', mode='r') as reading_data:
        file_data = json.load(reading_data)
except FileNotFoundError:
    url = 'https://opentdb.com/api.php?amount=10&type=boolean'
    my_request = requests.get(url=url)
    my_request.raise_for_status()
    results = my_request.json()['results']

    with open('data.json', mode='w') as dumping_data:
        json.dump(results, dumping_data, indent=4)
else:
    question_data_list = []
    for item in file_data:
        objectified_question = Question(item['question'], item['correct_answer'])
        question_data_list.append(objectified_question)
    quiz = Quiz(question_data_list)
    interface = QuizInterface(quiz)
    
    