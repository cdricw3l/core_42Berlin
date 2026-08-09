def ft_count_harvest_iterative() -> None:
    until_day: int = int(input("Days until harvest: "))
    day: int = 1
    for day in range(day, until_day + 1):
        print("Day ", day)
    print("Harvest time!")
