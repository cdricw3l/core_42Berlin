class GardenError(Exception):
    def __init__(self, msg: str = "Unknown plant error"):
        Exception.__init__(self, msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error"):
        GardenError.__init__(self, msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown plant error"):
        GardenError.__init__(self, msg)


if __name__ == "__main__":
    list_err: list[WaterError | PlantError] = [
            PlantError("The tomato plant is wilting!"),
            WaterError("Not enough water in the tank!")
    ]
    print('=== Custom Garden Errors Demo ===\n')
    for err in list_err:
        print(f"Testing {err.__class__.__name__}...")
        try:
            raise err
        except err.__class__ as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing catching all garden errors...")
    for err in list_err:
        try:
            raise err
        except GardenError as e:
            print(f"Caught {GardenError.__name__}: {e}")
    print("\nAll custom error types work correctly!")
