import random


class QuestionManager:
    def __init__(self, questions):
        self.questions = questions

    def get_random_question(self):
        return random.choice(self.questions)

    def get_questions_by_subject(self, subject):
        return [q for q in self.questions if q["subject"] == subject]

    def get_questions_by_category(self, category):
        return [q for q in self.questions if q["category"] == category]

    def get_questions_by_difficulty(self, difficulty):
        return [q for q in self.questions if q["difficulty"] == difficulty]
