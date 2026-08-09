class PlantError(Exception):
    def __init__(self, msg: str = "Unknown plant error"):
        Exception.__init__(self, msg)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    valide_list: list[str] = ["Tomato", "Lettuce", "Carrots"]
    invalide_list: list[str] = ["Tomato", "lettuce"]

    try:
        print("Testing valid plants...")
        print("Opening watering system")
        for valide in valide_list:
            water_plant(valide)
    except PlantError as err:
        print(f"Caught {err.__class__.__name__}: {err}")
    finally:
        print("Closing watering system")
    try:
        print("\nTesting invalid plants...")
        print("Opening watering system")
        for invalide in invalide_list:
            water_plant(invalide)
    except PlantError as err:
        print(f"Caught {err.__class__.__name__}: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
