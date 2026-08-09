import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player_list: list[str] = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam']
    if player_list:
        print(f"Initial list of players: {player_list}")
        capitalize_list: list[str] = [
            player.capitalize() for player in player_list]
        print(f"New list with all names capitalized: {capitalize_list}")
        capitalized_only_list: list[str] = [
            player for player in player_list if player == player.capitalize()]
        print(f"New list of capitalized names only: {capitalized_only_list}\n")
        score_list: dict[str, int] = {
            player: random.randrange(1, 500) for player in capitalize_list}
        print(f"Score dict: {score_list}")
        score_avg: float = round(
            sum([score_list[v] for v in score_list]) / len(score_list), 2)
        print(f"Score average is {score_avg}")
        high_score: dict[str, int] = {
            k: score_list[k] for k in score_list if score_list[k] > score_avg}
        print(f"High scores: {high_score}")
    else:
        print("player len list is equal to zero: add player!")
