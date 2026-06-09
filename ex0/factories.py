from abc import ABC, abstractmethod
import ex0.creature as c


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> c.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> c.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Flameling()

    def create_evolved(self) -> c.Creature:
        return c.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Aquabub()

    def create_evolved(self) -> c.Creature:
        return c.Torragon()
