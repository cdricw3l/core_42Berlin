import random


class Random_generation_error(ValueError):
    msg: str = "Achivement len list is equal to zero: add achivements!"

    def __init__(self, msg: str = msg):
        Exception.__init__(self, msg)


def gen_player_achievements(achivements: list[str], nba: int) -> set[str]:
    player_set: set[str] = set(random.sample(achivements, nba))
    return set(player_set)


def gen_ramdom_set_size(achivement_list: list[str]) -> int:
    try:
        nba: int = random.randrange(1, len(achivement_list))
    except ValueError:
        raise Random_generation_error
    return nba


if __name__ == "__main__":
    achivement_list: list[str] = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']

    try:
        print("=== Achievement Tracker System ===\n")
        nba: int = gen_ramdom_set_size(achivement_list)
        p1_name: str = "Cedric"
        p1_set: set[str] = gen_player_achievements(achivement_list, nba)
        print(f"Player {p1_name}: {p1_set}")
        p2_name: str = "Michel"
        p2_set: set[str] = gen_player_achievements(achivement_list, nba)
        print(f"Player {p2_name}: {p2_set}")
        p3_name: str = "Jean"
        p3_set: set[str] = gen_player_achievements(achivement_list, nba)
        print(f"Player {p3_name}: {p3_set}")
        p4_name: str = "Loic"
        p4_set: set[str] = gen_player_achievements(achivement_list, nba)
        print(f"Player {p4_name}: {p4_set}")
        p5_name: str = "Jacque"
        p5_set: set[str] = gen_player_achievements(achivement_list, nba)
        print(f"Player {p5_name}: {p5_set}\n")
        print(f"All distinct achievements: {set(achivement_list)}\n")
        print(
            f"Common achievements: "
            f"{set.intersection(p1_set, p2_set, p3_set, p4_set, p5_set)}\n")
        print(f"Only {p1_name} has: "
              f"{set(p1_set).difference(p2_set, p3_set, p4_set, p5_set)}")
        print(f"Only {p2_name} has: "
              f"{set(p2_set).difference(p1_set, p3_set, p4_set, p5_set)}")
        print(f"Only {p3_name} has: "
              f"{set(p3_set).difference(p1_set, p2_set, p4_set, p5_set)}")
        print(f"Only {p4_name} has: "
              f"{set(p4_set).difference(p1_set, p2_set, p3_set, p5_set)}")
        print(f"Only {p5_name} has: "
              f"{set(p5_set).difference(p1_set, p2_set, p3_set, p4_set)}\n")
        print(f"{p1_name} is missing: "
              f"{set(achivement_list).difference(p1_set)}")
        print(f"{p2_name} is missing: "
              f"{set(achivement_list).difference(p2_set)}")
        print(f"{p3_name} is missing: "
              f"{set(achivement_list).difference(p3_set)}")
        print(f"{p4_name} is missing: "
              f"{set(achivement_list).difference(p4_set)}")
        print(f"{p5_name} is missing: "
              f"{set(achivement_list).difference(p5_set)}\n")
    except (Random_generation_error) as e:
        print(e)
