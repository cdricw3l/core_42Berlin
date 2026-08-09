import sys


class Invalide_param(Exception):
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)


def get_key_value(split: list[str]) -> dict[str, int]:
    kv: dict[str, int] = {}
    try:
        key: str = split[0]
        value: int = int(split[1])
        kv.update({key: value})
    except IndexError:
        raise Invalide_param(f"Error - invalid parameter '{key}'")
    except ValueError as e:
        raise ValueError(f"Quantity error for '{key}': {e}")
    return kv


def parsing_arg(args: list[str]) -> dict[str, int]:
    if len(args) <= 0:
        raise Invalide_param("Parametre list is empty")
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            split: list[str] = arg.split(':')
            kv: dict[str, int] = get_key_value(split)
            # check if the key exist in invetory if no : dictionnary update
            if split[0] not in inventory:
                inventory.update(kv)
            else:
                print(f"Redundant item '{split[0]}'- discarding")
        except Invalide_param as e:
            print(e)
        except ValueError as e:
            print(e)
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    try:
        items: dict[str, int] = parsing_arg(args)
        print(f"Got inventory: {items}")
        print(f"Item list: {list(items.keys())}")
        total_quantity: int = sum(items.values())
        print(f"Total quantity of the {len(items)} items: {total_quantity}")
        biggest: dict[str, int] = {}
        smalest: dict[str, int] = {}
        for item in items:
            value: int = items.get(item, 0)
            # initialisatio of biggest dict data with the first key value
            if len(biggest) == 0:
                biggest.update({item: value})
            # initialisatio of smallest dict data with th first key value
            if len(smalest) == 0:
                smalest.update({item: value})
            if value > list(biggest.values())[0]:
                biggest.clear()
                biggest.update({item: value})
            if value < list(smalest.values())[0]:
                smalest.clear()
                smalest.update({item: value})
            print(f"Item {item} represents "
                  f"{round((value * 100) / total_quantity, 1)}%")
        print(
            f"Item most abundant: {list(biggest.keys())[0]} "
            f"with quantity"
            f" {biggest.get(list(biggest.keys())[0])}")
        print(f"Item least abundant: "
              f"{list(smalest.keys())[0]} "
              f"with quantity {smalest.get(list(smalest.keys())[0])}")
        items.update({"magic_item": 1})
        print(f"Updated inventory: {items}")
    except Invalide_param as e:
        print(e)
