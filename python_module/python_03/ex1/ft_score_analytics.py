import sys


class No_scores(Exception):
    msg: str = "No scores provided.\
 Usage: python3 ft_score_analytics.py <score1> <score2> ..."

    def __init__(self, msg: str = msg) -> None:
        Exception.__init__(self, msg)


class Scores:
    values: list[int]
    total_player: int
    total_score: int
    avg_score: float
    high_score: int
    low_score: int
    range_score: int

    def __init__(self, values: list[int]) -> None:
        self.values = values
        self.total_player = len(values)
        self.total_score = sum(self.values)
        self.avg_score = self.total_score / self.total_player
        self.high_score = max(self.values)
        self.low_score = min(self.values)
        self.range_score = self.high_score - self.low_score

    def __str__(self) -> str:
        return f"""Scores processed: {self.values}
Total player: {self.total_player}
Total score: {self.total_score}
Average score: {round(float(self.avg_score), 1)}
High score: {self.high_score}
Low score:: {self.low_score}
Score range: {self.range_score}\n"""


def process_arguments(argv: list[str]) -> list[int]:
    int_arr: list[int] = []
    if len(argv) == 0:
        raise No_scores
    for arg in argv:
        try:
            # list concatenation
            int_arr = int_arr + [int(arg)]
        except ValueError:
            print(f"invalid parameter: '{arg}'")
    if len(int_arr) == 0:
        raise No_scores
    return int_arr


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    print("=== Player Score Analytics ===")
    try:
        score_list: list[int] = process_arguments(args)
        data_score: Scores = Scores(score_list)
        print(data_score)
    except No_scores as e:
        print(f"{e}\n")
