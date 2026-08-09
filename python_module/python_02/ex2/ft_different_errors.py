def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    match operation_number:
        case 0:
            print(f"value: {int("abc")}")
        case 1:
            print(f"result = {1 / 0}")
        case 2:
            with open("/non/existent/file", "r+") as f:
                line = f.read()
                print(line)
        case 3:
            print(f"{'hello' + int(10)}")
        case _:
            print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i: int = 0
    while i <= 4:
        try:
            garden_operations(i)
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
                ) as err:
            print(f"Caught {err.__class__.__name__}: {err}")
        i += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
