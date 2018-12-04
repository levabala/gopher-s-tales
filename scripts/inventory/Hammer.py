from scripts.structures.Thing import Thing


def Hammer(): return {
    'name': 'hammer',
    'type': 'weapon',
    'weight': 0.7,
    'dice': (20, 1),  # 14 edges and 1 dice to roll
    'sm': 9,  # smashing damage
    'sl': 1,  # slicing damage
    'pr': 2,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
