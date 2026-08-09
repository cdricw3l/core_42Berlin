from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    ingredients_check: str = dark_validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients_check})"
