from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.healCapability import HealCapability
from ex1.transformCapability import TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature):
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, c1: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature):
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.__class__.__name__}' "
                f"for this aggressive strategy"
            )
        assert isinstance(creature, TransformCapability)

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError
        (
            f"Invalid Creature '{creature.__class__.__name__}' "
            f"for this defensive strategy"
        )
        assert isinstance(creature, HealCapability)

        print(creature.attack())
        print(creature.heal())
