from abc import ABC, abstractmethod


class Creature(ABC):
    """ Creature Abstract Base Class"""

    name: str
    type: str

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    """ Fire base creature """

    def __init__(self) -> None:
        super().__init__('Flameling', 'Fire')

    def attack(self) -> str:
        return f"{self.name} use Ember!"


class Pyrodon(Creature):
    """ Fire evolved creature """

    def __init__(self) -> None:
        super().__init__('Pyrodon', ' Fire/Flying')

    def attack(self) -> str:
        return f"{self.name} use Flamethrower!"


class Aquabub(Creature):
    """ Aqua base creature """

    def __init__(self) -> None:
        super().__init__('Aquabub', 'Water')

    def attack(self) -> str:
        return f"{self.name} use Water Gun!"


class Torragon(Creature):
    """ Aqua evolved creature """

    def __init__(self) -> None:
        super().__init__('Torragon', 'Water')

    def attack(self) -> str:
        return f"{self.name} use Hydro Pump!"


class CreatureFactory(ABC):
    """ Abstact base class for creature factory """

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """ Factory for fire creature """

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """ Factory for aqua creature """

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
