from scripts.structures.Thing import Thing


def BlackSword(): return {
    'name': 'black sword',
    'type': 'weapon',
    'dice': (14, 1),  # 14 edges and 1 dice to roll
    'sm': 2,  # smashing damage
    'sl': 7,  # slicing damage
    'pr': 4,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 3,  # acid damage
    **Thing(),
}
