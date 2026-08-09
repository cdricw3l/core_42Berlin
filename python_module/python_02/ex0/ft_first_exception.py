def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        temp_1: int = input_temperature("25")
        print(f"Temperature is now {temp_1}°C\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")

    print("Input data is 'abc'")
    try:
        temp_2: int = input_temperature("abc")
        print(f"Temperature is now {temp_2}°C", end="\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
