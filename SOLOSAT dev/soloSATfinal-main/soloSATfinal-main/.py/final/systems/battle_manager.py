class BattleManager:
    def __init__(self, player):
        self.player = player

    def answer(self, question, selected_answer):
        self.player.solved += 1

        if selected_answer == question["answer"]:
            self.player.correct += 1
            self.player.score += 100
            self.player.add_exp(question["exp"])
            return {"correct": True, "message": f"정답! +{question['exp']} EXP"}

        self.player.wrong += 1
        self.player.apply_penalty(question["penalty"])
        return {"correct": False, "message": f"오답! -{question['penalty']} Score"}

    def get_accuracy(self):
        if self.player.solved == 0:
            return 0.0
        return self.player.correct / self.player.solved * 100
