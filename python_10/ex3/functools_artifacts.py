from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"


class UnknownOperation(Exception):
    def __init__(self) -> None:
        super().__init__(f"{Color.RED}"
                         "Unknown operation for the spell reducer. "
                         "Allowed: 'add', 'multiply', 'min', 'max'"
                         f"{Color.RESET}")


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} hit {target} for {power} HP"


# `reducer` executes an operation and stores the value in the accumulator.
# It works like `reduce` in JavaScript.
def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case 'add':
            return reduce(lambda x, y: add(x, y), spells)
        case 'multiply':
            return reduce(lambda x, y: mul(x, y), spells)
        case 'max':
            return reduce(lambda x, y: max(x, y), spells)
        case 'min':
            return reduce(lambda x, y: min(x, y), spells)
        case _:
            raise UnknownOperation
    return 0


# `functools.partial` pre-fills parameters for a given function.
def partial_enchanter(base_enchantment:
                      Callable)\
                        -> dict[str, Callable]:
    return {'partial_enchantment': partial(base_enchantment, 50, 'Fireball')}


# lru_cache stock every return value of memoized_fibonacci
@lru_cache(maxsize=128, typed=False)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    return memoized_fibonacci(n - 1) +\
        memoized_fibonacci(n - 2) if n > 2 else 1


def spell_dispatcher() -> Callable:

    @singledispatch
    def dispatcher(*args) -> str:
        # `singledispatch` calls the registered function below.
        # If the first argument does not match a registered function,
        # it returns "Unknown spell type".
        return "Unknow spell type"

    @dispatcher.register(int)
    def _(damage_spell: int) -> str:

        return f"{damage_spell} damage"

    @dispatcher.register(str)
    def _(enchantement: str) -> str:
        return f"{enchantement}"

    @dispatcher.register(list)
    def _(element: list[Any]) -> str:
        return f"{" ".join([str(el) for el in element])}"

    return dispatcher


def spell_reducer_test(spell_powers: list[int]) -> None:
    print(f"\n{Color.YELLOW}Testing spell reducer...{Color.RESET}")
    try:
        print(f"expected: {sum(spell_powers)}, "
              f"result: {spell_reducer(spell_powers, 'add')}")

        def mul_item(spell_powers: list[int]) -> int:
            val: int = 1
            for v in spell_powers:
                val = val * v
            return val
        print(f"expected: {mul_item(spell_powers)}, "
              f"result: {spell_reducer(spell_powers, 'multiply')}")
        print(f"expected: {max(spell_powers)}, "
              f"result: {spell_reducer(spell_powers, 'max')}")
        print(f"expected: {min(spell_powers)}, "
              f"result: {spell_reducer(spell_powers, 'min')}")

        # Call `spell` reducer with a bad operation.
        # It must raise an error.
        print("Error expected below!!!")
        spell_reducer(spell_powers, 'bad operation')

    except Exception as e:
        print(f"{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")
    except UnknownOperation as e:
        print(e)


def partial_enchanter_test(target_list: list[str]) -> None:
    print(f"\n{Color.YELLOW}Testing partial enchanter...{Color.RESET}")
    try:
        partial: dict[
            str,
            Callable[[str], str]] = partial_enchanter(enchantment)
        f: Callable[[str], str] = partial['partial_enchantment']
        for target in target_list:
            print(f(target))
    except Exception as e:
        print(f"{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")


def memoized_fibonacci_test(int_list: list[int], info: bool) -> None:
    print(f"\n{Color.YELLOW}Testing Cached fibonacci...{Color.RESET}")
    try:
        for value in int_list:
            print(f"Fib({value}): {memoized_fibonacci(value)}")
            if info:
                print(memoized_fibonacci.cache_info())
    except Exception as e:
        print(f"\n{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")


def spell_dispatcher_test() -> None:
    print(f"\n{Color.YELLOW}Testing spell dispatcher...{Color.RESET}")
    try:
        dispatcher = spell_dispatcher()
        print(f"Damage spell: {dispatcher(42)}")
        print(f"Enchantment: {dispatcher('fireball')}")
        print(f"Multi-cast: {dispatcher([3, 'spells'])}")
        print(f"{Color.RED}{dispatcher(12.5)}{Color.RESET}")
    except Exception as e:
        print(f"\n{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")


if __name__ == "__main__":
    try:
        spell_powers = [33, 33, 16, 39, 44, 35]
        operations = ['add', 'multiply', 'max', 'min']
        spell_reducer_test(spell_powers)
        partial_enchanter_test(['Dragon', 'Goblin', 'Wizard', 'Knight'])
        memoized_fibonacci_test([0, 1, 2, 3, 11, 15, 18, 44], False)
        spell_dispatcher_test()
    except Exception as e:
        print(f"\n{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")
