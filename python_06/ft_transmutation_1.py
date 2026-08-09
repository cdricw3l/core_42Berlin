import alchemy.transmutation

# https://realpython.com/absolute-vs-relative-python-imports/


def ft_transmutation_1() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {
        alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    ft_transmutation_1()
