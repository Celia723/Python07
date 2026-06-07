from abc import ABC, abstractmethod
import ex0.creature as c
import ex0.healCapability as heal
import ex0.transformCapability as transform

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


class HealFactory(CreatureFactory):
    def create_base(self) -> heal.HealCapability:
        return heal.Sproutling()
    
    def create_evolved(self) -> heal.HealCapability:
        return heal.Bloomelle()


class TransformFactory(CreatureFactory):
    def create_base(self) -> transform.TransformCapability:
        return transform.Shiftling()
    
    def create_evolved(self) -> transform.TransformCapability:
        return transform.Morphagon()
            

