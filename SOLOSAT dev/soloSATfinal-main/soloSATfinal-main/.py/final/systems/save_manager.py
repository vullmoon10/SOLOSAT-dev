import json
import os


class SaveManager:
    def __init__(self, path="solosat_save.json"):
        self.path = path

    def save(self, player, difficulty, speedrun):
        data = {
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

    def exists(self):
        return os.path.exists(self.path)

    def load(self, player):
        if not self.exists():
            return None

        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)

        saved = data["player"]
        player.nickname = saved["nickname"]
        player.x = saved["x"]
        player.level = saved["level"]
        player.exp = saved["exp"]
        player.max_exp = saved["max_exp"]
        player.score = saved["score"]
        player.hp = saved["hp"]
        player.correct = saved["correct"]
        player.wrong = saved["wrong"]
        player.solved = saved["solved"]

        game = data.get("game", {})
        return {
            "difficulty": game.get("difficulty", "중"),
            "speedrun": game.get("speedrun", False),
        }
