from abc import ABC, abstractmethod
from ex0.creature_factory import Creature
from ex1.capabilities_factory import HealCapability, TransformCapability
from typing import cast


class Bad_combinaison(Exception):

    def __init__(self, name: str, strategy: str) -> None:
        super().__init__(f"Battle error, "
                         f"aborting tournament: Invalid Creature "
                         f"'{name}' for this {strategy} strategy")


class BattleStrategy(ABC):

    @abstractmethod
    def is_valide(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valide(self, creature: Creature) -> bool:
        if issubclass(creature.__class__, Creature):
            return True
        return False

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valide(self, creature: Creature) -> bool:
        if issubclass(creature.__class__, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:

        if self.is_valide(creature) is not True:
            raise Bad_combinaison(creature.name, "aggressive")
        bestiol = cast(TransformCapability, creature)
        print(bestiol.transform())
        print(bestiol.get_attack())
        print(bestiol.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valide(self, creature: Creature) -> bool:
        if issubclass(creature.__class__, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if self.is_valide(creature) is not True:
            raise Bad_combinaison(creature.name, "defensive")
        print(creature.attack())
        bestiol = cast(HealCapability, creature)
        print(bestiol.heal())
