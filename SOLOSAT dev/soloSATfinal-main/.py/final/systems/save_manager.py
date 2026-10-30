import json
import os


# 클래스 기능
class SaveManager:  # ?? ??? ??? ??
    # 함수 기능
    def __init__(self, path="solosat_save.json"):  # ?? ?? ?? ??
        self.path = path  # 변수 기능

    # 함수 기능
    def save(self, player, difficulty, speedrun):  # ?? ?? ?? ??
        data = {  # 변수 기능
            "player": {
                "nickname": player.nickname,
                "x": player.x,
                "level": player.level,
                "exp": player.exp,
                "max_exp": player.max_exp,
                "score": player.score,
                "hp": player.hp,
                "correct": player.correct,
                "wrong": player.wrong,
                "solved": player.solved,
            },
            "game": {
                "difficulty": difficulty,
                "speedrun": speedrun,
            },
        }
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 함수 기능
    def exists(self):  # ?? ?? ?? ??
        return os.path.exists(self.path)

    # 함수 기능
    def load(self, player):  # ?? ?? ????
        # 조건 분기
        if not self.exists():  # ??? ?? ?? ?? ??
            return None

        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)  # 변수 기능

        saved = data["player"]  # 변수 기능
        player.nickname = saved["nickname"]  # 변수 기능
        player.x = saved["x"]  # 변수 기능
        player.level = saved["level"]  # 변수 기능
        player.exp = saved["exp"]  # 변수 기능
        player.max_exp = saved["max_exp"]  # 변수 기능
        player.score = saved["score"]  # 변수 기능
        player.hp = saved["hp"]  # 변수 기능
        player.correct = saved["correct"]  # 변수 기능
        player.wrong = saved["wrong"]  # 변수 기능
        player.solved = saved["solved"]  # 변수 기능

        game = data.get("game", {})  # 변수 기능
        return {
            "difficulty": game.get("difficulty", "以?),
            "speedrun": game.get("speedrun", False),
        }
