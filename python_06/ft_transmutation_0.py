import alchemy.transmutation.recipes

# https://realpython.com/absolute-vs-relative-python-imports/


def ft_transmutation_0() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {
        alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    ft_transmutation_0()
