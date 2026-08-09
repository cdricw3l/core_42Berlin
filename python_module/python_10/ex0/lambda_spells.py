class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"

# A lambda function is an anonymous inline function.
# Use a lambda for simple inline logic.
# Use a regular function for more complex logic.
# Lambda syntax: lambda arguments: expression


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    # Example: `mages` is a list of dictionaries.
    # `x` represents each dictionary.
    # `x['power']` retrieves the value associated with the `'power'` key
    # and compares it to `min_power`.
    return (list(filter(lambda x: x['power'] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda x: f"* {x} *", spells)))


def mage_stats(mages: list[dict]) -> dict:
    return {

        # Here, `max(mages, key=lambda x: x['power'])` returns the dictionary
        # with the highest value for the `'power'` key.

        'max_power': int(max(mages, key=lambda x: x['power'])['power']),
        'min_power': int(min(mages, key=lambda x: x['power'])['power']),
        'avg_power': round(sum(map(
            lambda x: x['power'], mages)) / len(mages), 2)
    }


def test_artifact_sorter(artifacts: list[dict]) -> None:
    print(f"\n{Color.YELLOW}Testing artifact sorter...{Color.RESET}")
    try:
        sorted_artifacts: list[dict] = artifact_sorter(artifacts)
        print("Artifact sorted by 'power' level (descending):")
        for x, artifact in enumerate(sorted_artifacts):
            print(f"Artifact Number {x + 1}")
            print(f"Name: {artifact['name']}")
            print(f"Power: {artifact['power']}")
            print(f"Type: {artifact['type']}\n")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def test_power_filter(mages: list[dict], min_power: int) -> None:
    print(f"\n{Color.YELLOW}Testing power filter...{Color.RESET}")
    try:
        filtered_mages: list[dict] = power_filter(mages, min_power)
        print(f"Mages with power >= {min_power}:")
        for x, mage in enumerate(filtered_mages):
            print(f"Mage Number {x + 1}")
            print(f"Name: {mage['name']}")
            print(f"Power: {mage['power']}")
            print(f"Type: {mage['element']}\n")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def test_spell_transformer(spells: list[str]) -> None:
    print(f"\n{Color.YELLOW}Testing spell transformer...{Color.RESET}")
    try:
        spell_transformed: list[str] = spell_transformer(spells)
        for x, spell in enumerate(spell_transformed):
            print(f"Transformation number: {x + 1}: "
                  f"from {spells[x]} to {spell}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def test_mage_stats(mages: list[dict]) -> None:
    print(f"\n{Color.YELLOW}Testing mages stats display...{Color.RESET}")
    try:
        stats: dict = mage_stats(mages)
        print(f"Most powerful mage: {stats['max_power']}")
        print(f"Least powerful mage: {stats['min_power']}")
        print(f"Avg power : {stats['avg_power']}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    artifacts = [
        {
            'name': 'Ice Wand',
            'power': 86,
            'type': 'armor'
        },
        {
            'name': 'Wind Cloak',
            'power': 68,
            'type': 'weapon'
        },
        {
            'name': 'Ice Wand',
            'power': 120,
            'type': 'relic'
        },
        {
            'name': 'Shadow Blade',
            'power': 103,
            'type': 'relic'
        }
    ]
    mages = [
        {
            'name': 'Casey',
            'power': 100,
            'element': 'water'
        },
        {
            'name': 'Luna',
            'power': 74,
            'element': 'fire'
        },
        {
            'name': 'Morgan',
            'power': 62.568,
            'element': 'fire'
        },
        {
            'name': 'Phoenix',
            'power': 81.555,
            'element': 'wind'
        },
        {
            'name': 'Nova',
            'power': 74,
            'element': 'earth'
        }
    ]
    spells = ['tsunami', 'shield', 'fireball', 'lightning']
    try:
        # `test_artifact_sorter` takes a list of artifacts.
        test_artifact_sorter(artifacts)
        # `test_power_filter` takes a list of mages
# and a minimum power value.
        test_power_filter(mages, 74)
        # test_spell_transformer take list of spell
        test_spell_transformer(spells)
        # test_mage_stats take list of mage
        test_mage_stats(mages)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
