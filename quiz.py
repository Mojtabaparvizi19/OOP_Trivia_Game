import html


class Quiz:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.current_question = ''

    def still_got_question(self):
        if len(self.question_list) > self.question_number:
            return True

    def draw_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer: str):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True

        else:
            return False


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
