import random
import typing


class Random_generation_error(ValueError):
    msg: str = "Name len list is equal to zero: add achivements!"

    def __init__(self, msg: str):
        Exception.__init__(self, msg)


def gen_event(
        list_name: list[str],
        list_action: list[str]) -> typing.Generator[tuple[str, ...]]:
    if len(list_name) == 0 and len(list_action) == 0:
        raise Random_generation_error(
            "Name  and action list len are equal to zero:"
            " add Name and action!")
    if len(list_name) == 0:
        raise Random_generation_error(
            "Name list len is equal to zero: add Name!")
    if len(list_action) == 0:
        raise Random_generation_error(
            "Action list len  is equal to zero: add Action!")
    while list_name and list_action:
        r_name: str = random.choice(list_name)
        r_action: str = random.choice(list_action)
        yield tuple([r_name, r_action])


def consume_event(events: list[tuple[str, ...]]
                  ) -> typing.Generator[tuple[str, ...]]:
    while events:
        idx: int = random.randrange(len(events))
        value: tuple[str, ...] = events[idx]
        del events[idx]
        yield value


if __name__ == "__main__":
    list_name: list[str] = []
    action_list: list[str] = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "sleep", "swim", "release"]
    nb_event: int = 1000
    print("=== Game Data Stream Processor ===")
    try:
        gen = gen_event(list_name, action_list)
        for i in range(nb_event):
            try:
                value: tuple[str, ...] = next(gen)
                print(
                    f"Event {i}: "
                    f"Player {value[0]} "
                    f"did action run {value[1]}")
            except (StopIteration, IndexError):
                print("fin de l'iteration")
                break
        gen = gen_event(list_name, action_list)
        list_event: list[tuple[str, ...]] = [next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen),
                                             next(gen)]
        print(f"Built list of 10 events: {list_event}")
        for event in consume_event(list_event):
            print(f"Got event from list: {event}")
            print(f"Remains in list: {list_event}")
    except Random_generation_error as e:
        print(e)
