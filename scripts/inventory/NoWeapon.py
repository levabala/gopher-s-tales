from scripts.structures.Thing import Thing


def NoWeapon(): return {
    'name': 'no weapon',
    'type': 'weapon',
    'weight': 0,
    'dice': (0, 0),
    'sm': 0,  # smashing damage
    'sl': 0,  # slicing damage
    'pr': 0,  # piercing damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
