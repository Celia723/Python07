import ex1.new_factories as factories

if __name__ == "__main__":
    print("Testing Creature with healing capability")

    healing_factory = factories.HealFactory()

    print("base:")
    sproutling = healing_factory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print("evolved:")
    bloomelle = healing_factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal("nicho"))
    print()

    print("Testing Creature with transform capability")

    transform_factory = factories.TransformFactory()

    print("base:")
    shiftling = transform_factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())   

    print("evolved:")
    morphagon = transform_factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())
    print(morphagon.attack())
