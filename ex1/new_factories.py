import ex0.factories as factories
import ex1.healCapability as heal
import ex1.transformCapability as transform


class HealFactory(factories.CreatureFactory):
    def create_base(self) -> heal.Sproutling:
        return heal.Sproutling()

    def create_evolved(self) -> heal.Bloomelle:
        return heal.Bloomelle()


class TransformFactory(factories.CreatureFactory):
    def create_base(self) -> transform.Shiftling:
        return transform.Shiftling()

    def create_evolved(self) -> transform.Morphagon:
        return transform.Morphagon()
