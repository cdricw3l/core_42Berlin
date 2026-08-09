from alchemy.grimoire.dark_spellbook import dark_spell_record


def ft_kaboom_0() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(f"Testing record light spell: {
        dark_spell_record("Fantasy", "Earth wind fire")}")


if __name__ == "__main__":
    ft_kaboom_0()
