import alchemy.grimoire


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {
        alchemy.grimoire.light_spell_record(
            "Fantasy", "Earth wind fire")}")


if __name__ == "__main__":
    ft_kaboom_0()
