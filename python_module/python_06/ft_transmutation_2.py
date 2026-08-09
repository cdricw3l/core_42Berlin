import alchemy

# https://realpython.com/absolute-vs-relative-python-imports/


def ft_transmutation_2() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.recipes.lead_to_gold()}")


if __name__ == "__main__":
    ft_transmutation_2()
