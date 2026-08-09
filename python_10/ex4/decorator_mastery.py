import time
from typing import Callable
from functools import wraps


class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Doc string for help comprehension of  @wrapper """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)}")
        return result
    return wrapper


# https://stackoverflow.com/questions/61233508/parameterized-decorators-in-python
def power_validator(min_power: int) -> Callable:
    def validator(func: Callable):
        @wraps(func)
        # *args is a tuple of all argument passed to the fonction
        def wrapper(*args, **kwargs):
            if args[2] < min_power:
                return "Insufficient power for this spell"
            return func(*args)
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func):
        func.retry = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(args[0] - 1)
            except Exception:
                if func.retry == max_attempts:
                    print(f"Spell casting failed after "
                          f"{max_attempts} attempts")
                else:
                    print(f"Spell failed, retrying... (attempt "
                          f"{func.retry + 1}/{max_attempts})")
                    func.retry += 1
                    wrapper(args[0] - 1, **kwargs)
        return wrapper
    return retry


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.isalnum()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(ex_simulation_time: int) -> str:
    """ Doc string for @wrap decorator exemple """

    time.sleep(ex_simulation_time)
    return "Fireball cast!"


def spell_timer_test() -> None:
    try:
        # create a timer wrapper for fireball
        print(f"Casting {fireball.__name__}...")
        print(f"Result: {fireball(5)}")
    except (Exception, KeyboardInterrupt) as e:
        print(f"\n{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")


def power_validator_test(power: int) -> None:
    mage: MageGuild = MageGuild()
    print(mage.cast_spell("hello", power))


@retry_spell(11)
def max_retry(nb_of_err_simulation: int) -> None:
    if nb_of_err_simulation >= 0:
        raise Exception
    else:
        print("Waaaaaaagh spelled !")


def retrying_spell_test(nb_of_err_simulation: int) -> None:
    print(f"\n{Color.YELLOW}Testing retrying spell...{Color.RESET}")
    max_retry(nb_of_err_simulation)


def mage_guild_test() -> None:
    print(f"\n{Color.YELLOW}Testing MageGuild...{Color.RESET}")
    mage: MageGuild = MageGuild()
    print(mage.validate_mage_name("berlimage"))
    print(mage.validate_mage_name("!hello"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 2))


if __name__ == "__main__":
    print(f"\n{Color.YELLOW}Testing spell timer...{Color.RESET}")
    spell_timer_test()
    retrying_spell_test(10)
    mage_guild_test()
