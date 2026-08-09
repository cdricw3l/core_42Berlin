import math


# value in set can be modified so set doesnt accept list an dictionnary
# but set tiself can be modified. we can add or delete value in set.
# every element in set can be modified

class Invalid_syntax(Exception):
    def __init__(self, msg: str = "Invalid syntax") -> None:
        Exception.__init__(self, msg)


class Set_data():
    __points: tuple[float, ...]

    def __init__(self, points: tuple[float, ...]) -> None:
        self.__points = points

    def display_set_data(self) -> None:
        print(f"Got a first tuple: {self.__points}")
        print(
            f"It includes: X={self.__points[0]},"
            f"Y={self.__points[1]},"
            f"Z={self.__points[2]}"
        )

    def display_distance(self) -> None:
        distance: float = math.sqrt((self.__points[0])**2
                                    + (self.__points[1])**2
                                    + (self.__points[2])**2
                                    )
        print(f"Distance to center: {round(distance, 4)}\n")

    def get_set(self) -> tuple[float, ...]:
        return tuple(self.__points)


def distance_between_two_set(set_1: Set_data, set_2: Set_data) -> None:
    s1: tuple[float, ...] = set_1.get_set()
    s2: tuple[float, ...] = set_2.get_set()
    distance: float = math.sqrt((s2[0] - s1[0])**2
                                + (s2[1] - s1[1])**2
                                + (s2[2] - s1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


def get_player_pos() -> tuple[float, ...]:

    while (1):
        user_input: str = input(
            "Enter new coordinates as floats"
            " in format 'x,y,z': "
        )
        if user_input.count(",") != 2:
            raise Invalid_syntax
        split_input: list[str] = user_input.split(",")
        for value in split_input:
            try:
                float(value)
            except ValueError as e:
                raise ValueError(f"Error on parameter '{value}': {e}")
        arg_set: tuple[float, ...] = (
            float(split_input[0]),
            float(split_input[1]),
            float(split_input[2]))
        return arg_set


# input getter whith label printing
def get_set(label: str) -> tuple[float, ...]:
    print(f"Get a {label} set of coordinates")
    # infinit loop utils good set
    while 1:
        try:
            set: tuple[float, ...] = get_player_pos()
            return set
        except (Invalid_syntax, ValueError) as e:
            print(f"{e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    set_1: tuple[float, ...] = get_set("first")
    data_set_1: Set_data = Set_data(set_1)
    data_set_1.display_set_data()
    data_set_1.display_distance()
    set_2: tuple[float, ...] = get_set("second")
    data_set_2: Set_data = Set_data(set_2)
    distance_between_two_set(data_set_1, data_set_2)
