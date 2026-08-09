import alchemy


def alembic_4() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(alchemy.create_earth())


if __name__ == "__main__":
    alembic_4()
