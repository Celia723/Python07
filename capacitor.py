# capacitor.py
# Este archivo va en la raíz del repositorio

import ex1.factories as factories

if __name__ == "__main__":
    
    # =========================================================================
    # 1. TESTEO DE CRIATURAS CON CAPACIDAD DE CURACIÓN (HEALING)
    # =========================================================================
    print("Testing Creature with healing capability")
    
    # Creamos la factoría de curación
    healing_factory = factories.HealingCreatureFactory()
    
    # --- Criatura Base ---
    print("base:")
    sproutling = healing_factory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    
    # --- Criatura Evolucionada ---
    print("evolved:")
    bloomelle = healing_factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())
    
    # =========================================================================
    # 2. TESTEO DE CRIATURAS CON CAPACIDAD DE TRANSFORMACIÓN
    # =========================================================================
    print("Testing Creature with transform capability")
    
    # Creamos la factoría de transformación
    transform_factory = factories.TransformCreatureFactory()
    
    # --- Criatura Base ---
    print("base:")
    shiftling = transform_factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())          # Ataque normal
    print(shiftling.transform())       # Se transforma (activa estado)
    print(shiftling.attack())          # Ataque potenciado (gracias a tu estado)
    print(shiftling.revert())          # Vuelve a la normalidad
    
    # --- Criatura Evolucionada ---
    print("evolved:")
    morphagon = transform_factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())          # Ataque normal
    print(morphagon.transform())       # Se transforma (activa estado)
    print(morphagon.attack())          # Ataque devastador (gracias a tu estado)
    print(morphagon.revert())          # Vuelve a la normalidad