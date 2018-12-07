from scripts.structures.Thing import Thing


def FireBall(): return {
    'name': 'fire ball',
    'type': 'weapon',
    'weight': 0.1,
    'dice': (2, 7),  # 14 edges and 1 dice to roll
    'sm': 4,  # smashing damage
    'sl': 0,  # slicing damage
    'pr': 0,  # piercing damage
    'fr': 8,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
