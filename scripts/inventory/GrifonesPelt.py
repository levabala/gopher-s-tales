from scripts.structures.Thing import Thing


def GrifonesPelt(): return {
    'name': 'grifone pelt',
    'type': 'body armor',
    'weight': 0.7,
    'sm': 8,  # smash resistance
    'sl': 8,  # slice resistance
    'pr': 8,  # pirce resistance
    'fr': -4,  # fire resistance
    'ac': 2,  # acid resistance
    **Thing(),
}
