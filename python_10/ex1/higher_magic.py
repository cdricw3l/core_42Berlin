
from typing import Callable


class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"


# Conditional function for the conditional_caster
def condition_test(target: str, power: int) -> bool:
    if target == 'Dragon' and power > 10 or target == 'Wizard' and power > 10:
        return True
    else:
        return False


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def attack(target: str, power: int) -> str:
    return f"Fireball hit {target} for {power} HP"


def strong_attack(target: str, power: int) -> str:
    return f"Strong Fireball hit {target} for {power * 10} HP"


# spell1 and spell2 are the two functions that should be combined.
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    # target and power are the two arguments of our new combinator function.
    def combiner(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combiner


# base_spell is our base function, and multiplier is the multiplier to apply.
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    # `target` and `power` are the two arguments of our new function.
    def amplifier(target: str, power: int) -> Callable:
        if multiplier > 0:
            return base_spell(target, power * multiplier)
        else:
            return base_spell(target, power)
    return amplifier


# `condition` is the function used to determine if `spell` should be called.
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


# `spells` is a list of functions that will be called sequentially
# by the `sequence` function with the `target` and `power` arguments
def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def spells_combinaison_test(target_power: dict[str, int],
                            spell1: Callable,
                            spell2: Callable) -> None:
    try:
        combined: Callable = spell_combiner(spell1, spell2)
        print(f"\n{Color.YELLOW}Combine two spells test:{Color.RESET}\n")
        for target in target_power:
            if target_power[target] > 0:
                comb: tuple = combined(target, target_power.get(target))
            print(f"{Color.RED}{comb[0]}, {Color.GREEN}{comb[1]}{Color.RESET}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def amplifier_test(target_power: dict[str, int], spell1: Callable):

    try:
        print(f"\n{Color.YELLOW}Amplify spell power test:{Color.RESET}")
        print("\nBefor amplification:")
        for target in target_power:
            print(spell1(target, target_power.get(target)))
        print("\nAfter amplification:")
        amplificator: Callable = power_amplifier(spell1, 3)
        for target in target_power:
            print(amplificator(target, target_power.get(target)))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def conditional_caster_test(target_power: dict[str, int],
                            condition: Callable, spell1: Callable):

    try:
        print(f"\n{Color.YELLOW}Cast spell conditionally test"
              "(condition: target = dragon or Wizard, power > 10):"
              f"{Color.RESET}")
        conditional: Callable = conditional_caster(condition, spell1)
        for target in target_power:
            print(conditional(target, target_power.get(target)))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def spell_sequence_test(target_power: dict[str, int], spells: list[Callable]):

    try:
        print(f"\n{Color.YELLOW}Create spell sequence:{Color.RESET}")
        sequences: Callable = spell_sequence(spells)
        for target in target_power:
            print(f"For {target}:")
            sequences_list = sequences(target, target_power.get(target))
            for sequence in sequences_list:
                print(f"\t{sequence}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":

    test_targets = {'Dragon': 11, 'Goblin': 20, 'Wizard': 14, 'Knight': 1}
    try:
        spells_combinaison_test(test_targets, attack, heal)
        amplifier_test(test_targets, attack)
        conditional_caster_test(test_targets, condition_test, strong_attack)
        spell_sequence_test(test_targets, [attack, strong_attack, heal])
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
