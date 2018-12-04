from scripts.structures.Thing import Thing


def GrifonClaws(): return {
    'name': 'hammer',
    'type': 'weapon',
    'weight': 0.7,
    'dice': (10, 2),  # 14 edges and 1 dice to roll
    'sm': 2,  # smashing damage
    'sl': 5,  # slicing damage
    'pr': 6,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
