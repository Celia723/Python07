import ex0.factories as factories

if __name__ == "__main__":
    print("Testing factory")
    flame_factoy = factories.FlameFactory()
    aqua_factory = factories.AquaFactory()

    Flameling = flame_factoy.create_base()
    print(Flameling.describe())
    print(Flameling.attack())

    Pyrodon = aqua_factory.create_evolved()
    print(Pyrodon.describe())
    print(Pyrodon.attack())

    print()
    print("Testing factory")
    Aquabub = aqua_factory.create_base()
    print(Aquabub.describe())
    print(Aquabub.attack())

    Torragon = aqua_factory.create_evolved()
    print(Torragon.describe())
    print(Torragon.attack())

    print()
    print("Testing battle")
    print(Flameling.describe())
    print("vs.")
    print(Aquabub.describe())
    print("fight!")
    print(Flameling.attack())
    print(Aquabub.attack())
