from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> bool:
    print("Testing factory")
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())
        print()
    except Exception as e:
        print(f"Factory error: {e}")
        return False
    return True


def fight(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    flamme_base = factory_1.create_base()
    aqua_base = factory_2.create_base()

    print(f"{flamme_base.describe()}\n vs.\n{aqua_base.describe()}\n fight!")
    print(flamme_base.attack())
    print(aqua_base.attack())


if __name__ == "__main__":

    flamme_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()

    if test_factory(
        flamme_factory) is True and test_factory(
            aqua_factory) is True:
        fight(flamme_factory, aqua_factory)
