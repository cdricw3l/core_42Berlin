
def validate_ingredients(ingredients: str) -> str:
    # Deferred import or lazy import
    # other way top level managment
    from . import light_spell_allowed_ingredients
    valide: bool = False
    string: str = ""
    arr_str: list[str] = ingredients.split(' ')
    size: int = len(arr_str) - 1
    for ingredient in arr_str:
        allowed: list[str] = [x.capitalize()
                              for x
                              in light_spell_allowed_ingredients()]
        if ingredient.capitalize() in allowed:
            valide = True
        if arr_str.index(ingredient) == size - 1:
            string = string + f"{ingredient} and "
        elif arr_str.index(ingredient) == size:
            string = string + f"{ingredient} "
        else:
            string = string + f"{ingredient}, "
    if valide is True:
        string = string + "- VALIDE"
    else:
        string = string + "- INVALIDE"
    return string
