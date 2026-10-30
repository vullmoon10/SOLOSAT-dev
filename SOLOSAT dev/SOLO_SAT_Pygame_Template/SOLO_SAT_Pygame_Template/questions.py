# questions.py
#문제는 게임 로직과 분리해. 앞으로 과목별 문제를 늘릴 때 이 파일만 주로 수정하면 돼.

QUESTIONS = [
    {
        "id": "math_001",
        "subject": "수학",
        "difficulty": "easy",
        "q": "3 + 8 = ?",
        "choices": ["21", "12", "10", "11"],
        "answer": 3,
        "time": 30,
    },
    {
        "id": "math_002",
        "subject": "수학",
        "difficulty": "easy",
        "q": "82 - 36 = ?",
        "choices": ["56", "54", "46", "36"],
        "answer": 2,
        "time": 30,
    },
    {
        "id": "math_003",
        "subject": "수학",
        "difficulty": "medium",
        "q": "어떤 수에서 128을 뺐더니 275가 되었습니다.",
        "choices": ["393", "413", "403", "147"],
        "answer": 0,
        "time": 45,
    },
    {
        "id": "math_004",
        "subject": "수학",
        "difficulty": "easy",
        "q": "7 + 8 = ?",
        "choices": ["16", "25", "15", "14"],
        "answer": 2,
        "time": 25,
    },
    {
        "id": "math_005",
        "subject": "수학",
        "difficulty": "medium",
        "q": "어떤 수에 248을 더했더니 315가 되었습니다.",
        "choices": ["811", "67", "563", "801"],
        "answer": 1,
        "time": 45,
    },
]


def get_random_question(difficulty=None):
    """난도에 맞는 문제를 하나 반환한다."""
    import random

    pool = [
        question
        for question in QUESTIONS
        if difficulty is None
        or question["difficulty"] == difficulty
    ]

    if not pool:
        pool = QUESTIONS

    return random.choice(pool)

# answer는 정답 선택지의 인덱스야. 첫 번째 선택지는 0, 네 번째 선택지는 3이야.

# [수정 가능] 문제를 추가할 때는 id를 중복하지 말고, choices를 4개로 유지하고, 정답 인덱스가 실제 정답과 일치하도록 해.