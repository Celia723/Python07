import ex0.factories as factories
import ex1.healCapability as heal
import ex1.transformCapability as transform
from ex0.creature import Creature


class HealFactory(factories.CreatureFactory):
    def create_base(self) -> Creature:
        return heal.Sproutling()

    def create_evolved(self) -> Creature:
        return heal.Bloomelle()


class TransformFactory(factories.CreatureFactory):
    def create_base(self) -> Creature:
        return transform.Shiftling()

    def create_evolved(self) -> Creature:
        return transform.Morphagon()
