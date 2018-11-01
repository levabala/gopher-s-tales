from scripts.structures.Thing import Thing


def Sword(): return {
    'name': 'sword',
    'type': 'weapon',
    'dice': (12, 1),  # 12 edges and 1 dice to roll
    'sm': 1,  # smashing damage
    'sl': 6,  # slicing damage
    'pr': 3,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
