from scripts.structures.Thing import Thing


def RustSword(): return {
    'name': 'rust sword',
    'type': 'weapon',
    'weight': 0.35,
    'dice': (8, 1),
    'sm': 1,  # smashing damage
    'sl': 3,  # slicing damage
    'pr': 2,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 2,  # acid damage
    **Thing(),
}
