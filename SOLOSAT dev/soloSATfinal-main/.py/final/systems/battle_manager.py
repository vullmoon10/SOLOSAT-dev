# 클래스 기능
class BattleManager:  # ?? ??? ?? ??
    # 함수 기능
    def __init__(self, player):  # ?? ?? ?? ??
        self.player = player  # 변수 기능

    # 함수 기능
    def answer(self, question, selected_answer):  # ?? ??? ?? ??
        self.player.solved += 1

        # 조건 분기
        if selected_answer == question["answer"]:  # ?? ?? ?? ??
            self.player.correct += 1
            self.player.score += 100
            self.player.add_exp(question["exp"])
            return {"correct": True, "message": f"?뺣떟! +{question['exp']} EXP"}

        self.player.wrong += 1
        self.player.apply_penalty(question["penalty"])
        return {"correct": False, "message": f"?ㅻ떟! -{question['penalty']} Score"}

    # 함수 기능
    def get_accuracy(self):  # ??? ??
        # 조건 분기
        if self.player.solved == 0:  # ??? ?? ?? ?? ??
            return 0.0
        return self.player.correct / self.player.solved * 100
