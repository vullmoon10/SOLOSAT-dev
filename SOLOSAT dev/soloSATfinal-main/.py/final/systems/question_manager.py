import random


# 클래스 기능
class QuestionManager:  # ?? ??? ?? ??
    # 함수 기능
    def __init__(self, questions):  # ?? ?? ?? ??
        self.questions = questions  # 변수 기능

    # 함수 기능
    def get_random_question(self):  # ??? ?? ??
        return random.choice(self.questions)

    # 함수 기능
    def get_questions_by_subject(self, subject):  # ??? ?? ??
        return [q for q in self.questions if q["subject"] == subject]

    # 함수 기능
    def get_questions_by_category(self, category):  # ??? ?? ??
        return [q for q in self.questions if q["category"] == category]

    # 함수 기능
    def get_questions_by_difficulty(self, difficulty):  # ???? ?? ??
        return [q for q in self.questions if q["difficulty"] == difficulty]
