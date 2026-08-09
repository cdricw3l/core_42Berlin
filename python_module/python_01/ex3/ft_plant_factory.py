class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old"
        )

    def grow(self, grow: float) -> None:
        self._height += grow

    def age(self, age: int) -> None:
        self._age += age


if __name__ == "__main__":
    list_plants: list[Plant] = [
        Plant("rose", 25.0, 30), Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 365), Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in list_plants:
        print("Created:", end=" ")
        plant.show()
