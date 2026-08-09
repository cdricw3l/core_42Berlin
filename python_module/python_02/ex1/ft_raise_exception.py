def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp > 40:
        raise ValueError("100°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError("-50°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    try:
        print("Input data is '25'")
        temp_1: int = input_temperature("25")
        print(f"Temperature is now {temp_1}°C\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")

    try:
        print("Input data is 'abc'")
        temp_2: int = input_temperature("abc")
        print(f"Temperature is now {temp_2}°C", end="\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")

    try:
        print("Input data is '100'")
        temp_3: int = input_temperature("100")
        print(f"Temperature is now {temp_3}°C", end="\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")

    try:
        print("Input data is '-50'")
        temp_4: int = input_temperature("-50")
        print(f"Temperature is now {temp_4}°C", end="\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
