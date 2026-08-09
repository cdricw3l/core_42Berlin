from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex2.strategy import \
    BattleStrategy, NormalStrategy, \
    AggressiveStrategy, DefensiveStrategy, Bad_combinaison


Warrior = tuple[CreatureFactory, BattleStrategy]


def get_strategy_name(strategy:  BattleStrategy) -> str:
    if isinstance(strategy, AggressiveStrategy):
        return 'aggressive'
    if isinstance(strategy, DefensiveStrategy):
        return 'defensive'
    return ""


def battle(opponant: list[tuple[CreatureFactory, BattleStrategy]]) -> bool:
    print(f"*** Tournament ***\n{len(opponant)} opponents involved\n")
    creatures_strategies: dict[Warrior, list[Warrior]] = {}

    # match making:
    # create a dictionnary where:
    # key is a Warrior (tuple creature_factory/strategie)
    # and value the list of Warrior
    for i in range(len(opponant)):
        warrior: Warrior = opponant[i]
        opponant_list: list[Warrior] = []
        for j in range(i + 1, len(opponant)):
            opponant_list.append(opponant[j])
        if len(opponant_list) > 0:
            creatures_strategies.update({warrior: opponant_list})

    for warrior_1 in creatures_strategies:
        # initialise the first factory
        warrior_1_factory: CreatureFactory = warrior_1[0]
        # create the first creature
        creature_1 = warrior_1_factory.create_base()
        # get the list of opponant of warrior 1
        opponant_list = creatures_strategies[warrior_1]
        # strategie linked to the warrior 1
        warrior_1_strategie = warrior_1[1]
        # loop inside the opponant list
        for warrior_2 in opponant_list:
            print("* Battle *")
            # create the factory of the opponant
            warrior_2_factory: CreatureFactory = warrior_2[0]
            # create the opponant
            creature_2 = warrior_2_factory.create_base()
            opponant_strategie = warrior_2[1]
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            if opponant_list.index(warrior_2) < len(opponant_list):
                print(" now fight!")
            try:
                if warrior_1_strategie\
                        .is_valide(creature_1) is False:
                    raise Bad_combinaison(creature_1.name,
                                          get_strategy_name(
                                              warrior_1_strategie))
                if opponant_strategie\
                        .is_valide(creature_2) is False:
                    raise Bad_combinaison(creature_1.name,
                                          get_strategy_name(
                                              opponant_strategie))
                warrior_1_strategie.act(creature_1)
                opponant_strategie.act(creature_2)
            except Bad_combinaison as e:
                print(e)
                return False
            if opponant.index(warrior_1) < len(opponant) - 2:
                print()
    return True


if __name__ == "__main__":

    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()
    heal_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()

    agressive: AggressiveStrategy = AggressiveStrategy()
    defensive: DefensiveStrategy = DefensiveStrategy()
    normal: NormalStrategy = NormalStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle_1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, normal),
        (heal_factory, defensive)
    ]
    battle(battle_1)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle_2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, agressive),
        (heal_factory, defensive)
    ]

    battle(battle_2)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle_3: list[tuple[CreatureFactory, BattleStrategy]] = [
        (aqua_factory, normal),
        (heal_factory, defensive),
        (transform_factory, agressive),
    ]

    battle(battle_3)
