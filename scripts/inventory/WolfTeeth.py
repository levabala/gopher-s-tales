from scripts.structures.Thing import Thing


def WolfTeeth(): return {
    'name': 'wolf teeth',
    'type': 'weapon',
    'weight': 0.3,
    'dice': (5, 2),  # 14 edges and 1 dice to roll
    'sm': 2,  # smashing damage
    'sl': 7,  # slicing damage
    'pr': 3,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
