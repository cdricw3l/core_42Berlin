class Plant:
    _name: str
    _height: float = 0.0
    _age: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        if height >= 0:
            self._height = height
        if age >= 0:
            self._age = age
        print(f"Plant created: {self._name}:", end=" ")
        print(f"{round(self._height, 2)}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, grow: float) -> None:
        if grow < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height += grow
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age += age
            print(f"Age updated: {self.get_age()} days")

    def show(self):
        print(
            f"Current state: {self._name}: "
            f"{self.get_height()}cm,",
            f"{self.get_age()} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(end="\n")
    rose.set_height(10)
    rose.set_age(20)
    print(end="\n")
    rose.set_height(-10)
    rose.set_age(-20)
    print(end="\n")
    rose.show()
