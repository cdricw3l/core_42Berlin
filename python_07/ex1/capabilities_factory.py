from abc import ABC, abstractmethod
from ex0.creature_factory import CreatureFactory, Creature


class HealCapability(ABC):
    """
        Heal Abstract Base Class
        for creature who can heal
    """

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    """
        TransformCapability Abstract Base Class
        for creature who can evolve
    """

    __attack: str

    def __init__(self) -> None:
        self.__attack = 'attacks normally.'

    def set_attack(self, attack: str) -> None:
        self.__attack = attack

    def get_attack(self) -> str:
        return f"{self.__attack}"

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    """ Sprouling creature who can heal """

    def __init__(self) -> None:
        super().__init__('Sproutling', 'Grass')

    def attack(self) -> str:
        return f"{self.name} use Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """ Bloomelle creature who can heal """

    def __init__(self) -> None:
        super().__init__('Bloomelle', 'Grass/Fairy')

    def attack(self) -> str:
        return f"{self.name} use Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """
        Shiftling creature who can transform.
        Transformation change the attack type
        via set_attack methode
    """

    def __init__(self) -> None:
        super().__init__('Shiftling', 'Normal')
        self.set_attack(f"{self.name} attacks normally.")

    def attack(self) -> str:
        return f"{self.get_attack()}"

    def transform(self) -> str:
        self.set_attack(f"{self.name} performs a boosted strike!")
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.set_attack(f"{self.name} attacks normally.")
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):

    """
        Shiftling creature who can transform.
        Transformation change the attack type
        via set_attack methode

    """

    def __init__(self) -> None:
        super().__init__('Morphagon', 'Normal/Dragon')
        self.set_attack(f"{self.name} attacks normally.")

    def attack(self) -> str:
        return f"{self.name} {self.get_attack()}"

    def transform(self) -> str:
        self.set_attack("unleashes a devastating morph strike!")
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.set_attack("attacks normally.")
        return f"{self.name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    """ Create Creature whith Healing Attribute """

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """ Create Creature whith Transform Attribute """

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
