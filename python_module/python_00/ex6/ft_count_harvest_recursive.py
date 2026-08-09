def ft_count_harvest_recursive() -> None:
    until_day: int = int(input("Days until harvest: "))

    def recusive_count(day: int) -> None:
        if (day > 1):
            recusive_count(day - 1)
        print("Day ", day)
    recusive_count(until_day)
    print("Harvest time!")
