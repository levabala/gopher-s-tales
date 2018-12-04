from scripts.structures.Thing import Thing


def FireBreath(): return {
    'name': 'fire breath',
    'type': 'weapon',
    'weight': 0.1,
    'dice': (5, 4),  # 14 edges and 1 dice to roll
    'sm': 3,  # smashing damage
    'sl': 0,  # slicing damage
    'pr': 0,  # piercing damage
    'fr': 7,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
