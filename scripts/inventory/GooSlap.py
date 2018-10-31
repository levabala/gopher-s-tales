from scripts.structures.Thing import Thing


def GooSlap(): return {
    'name': 'goo slap',
    'type': 'weapon',
    'dice': (2, 5),  # 2 edges and 5 dices to roll
    'sm': 1,  # smashing damage
    'sl': 0,  # slicing damage
    'pr': 0,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 7,  # acid damage
    **Thing(),
}
