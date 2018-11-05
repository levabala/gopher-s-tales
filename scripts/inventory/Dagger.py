from scripts.structures.Thing import Thing


def Dagger(): return {
    'name': 'dagger',
    'type': 'weapon',
    'weight': 0.1,
    'dice': (3, 3),  # 3 edges and 3 dices to roll
    'sm': 0,  # smashing damage
    'sl': 2,  # slicing damage
    'pr': 3,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
