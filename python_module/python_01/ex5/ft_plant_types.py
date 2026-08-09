class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def __set_height(self, grow: float) -> None:
        self._height += grow

    def __set_age(self, age: int) -> None:
        self._age += age

    def grow(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__set_height(height)

    def age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__set_age(new_age)

    def show(self, custom_msg: list[str]) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._age} days old"
        )
        if custom_msg:
            for msg in custom_msg:
                print(msg)


class Flower(Plant):
    _color: str
    _blooming_status: int

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming_status = 0

    def show(self):
        if (self._blooming_status == 0):
            bloom_msg = f"{self._name} has not bloomed yet"
        else:
            bloom_msg = f"{self.get_name()} is blooming beautifully!"
        super().show([
            f"Color: {self._color}",
            bloom_msg
        ])

    def bloom(self) -> None:
        self._blooming_status = 1


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
            self, name: str, height: float, age: int, diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter

    def show(self):
        super().show([f"Trunk diameter: {round(self._trunk_diameter)}cm"])

    def produce_shade(self, long: float, wide: float):
        print(
            f"Tree Oak now produces a shade of {round(long, 2)}cm long",
            f"and {round(wide, 2)}cm wide."
        )


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
            self, name: str, height: float, age: int,
            harvest_season: str, nutritional_value: int
            ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show([
            f"Harvest season: {self._harvest_season}",
            f"Nutritional value: {self._nutritional_value}"
        ])

    def set_nutritional_value(self, value: int) -> None:
        self._nutritional_value += value

    def grow(self, height: float) -> None:
        super().grow(height)
        self.set_nutritional_value(self.get_age() - 10)

    def age(self, age: int) -> None:
        super().age(age)
        self.set_nutritional_value(self.get_age() - 10)


if __name__ == "__main__":

    print("=== Garden Security System ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print(end="\n")
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade(200.0, 5)
    print(end="\n")
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.grow(42)
    vegetable.age(20)
    vegetable.show()
