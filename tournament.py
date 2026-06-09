from ex0.factories import AquaFactory, FlameFactory
from ex1.new_factories import HealFactory, TransformFactory
from ex2.battleStrategy import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def run_tournament(opponents: list) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    combatans = []

    for factory, strategy in opponents:

        creature = factory.create_base()
        combatans.append((creature, strategy))
    for i in range(len(combatans)):
        for j in range(i + 1, len(combatans)):

            c1, strat1 = combatans[i]
            c2, strat2 = combatans[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    opponents1 = [
        (FlameFactory(), NormalStrategy()),
        (HealFactory(), DefensiveStrategy())
    ]
    run_tournament(opponents1)
    print()

    print("Torunament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    opponents2 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealFactory(), DefensiveStrategy())
    ]
    run_tournament(opponents2)
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    opponents3 = [
        (AquaFactory(), NormalStrategy()),
        (HealFactory(), DefensiveStrategy()),
        (TransformFactory(), AggressiveStrategy())
    ]
    run_tournament(opponents3)
