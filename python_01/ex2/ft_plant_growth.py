class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 2)}cm, {self._age} days old"
        )

    def grow(self, grow: float) -> None:
        self._height += grow

    def age(self, age: int) -> None:
        self._age += age


if __name__ == "__main__":
    plan = Plant("Rose", 25, 30)
    initial_heigth = plan._height
    print("=== Garden Plant Growth ===")
    plan.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plan.age(1)
        plan.grow(0.8)
        plan.show()
    print(f"Growth this week: {round(plan._height - initial_heigth, 2)}cm")
