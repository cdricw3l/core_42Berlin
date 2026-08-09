class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":

    plants_list: list[Plant] = []
    plants_list.append(Plant("Rose", 25, 30))
    plants_list.append(Plant("Sunflower", 80, 45))
    plants_list.append(Plant("Cactus", 15, 120))
    print("=== Garden Plant Registry ===")
    for plant in plants_list:
        plant.show()
