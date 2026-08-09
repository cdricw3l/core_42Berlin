# relative import from the parent folder
from .. import potion, elements
# absolut import from top of the project
from elements import create_fire


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{
        elements.create_air()}' and '{
            potion.strength_potion()}' mixed with '{
                create_fire()}"
