from ex0.creature import Creature
from abc import ABC, abstractmethod


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.is_transform: int = 0

    def attack(self) -> str:
        if self.is_transform == 0:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.is_transform = 1
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transform = 0
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transform = 0

    def attack(self) -> str:
        if self.is_transform == 0:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.is_transform = 1
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transform = 0
        return f"{self.name}  stabilizes its form."
