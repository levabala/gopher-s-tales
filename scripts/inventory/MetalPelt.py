from scripts.structures.Thing import Thing


def MetalPelt(): return {
    'name': 'metal pelt',
    'type': 'body armor',
    'weight': 0.5,
    'sm': 3,  # smash resistance
    'sl': 8,  # slice resistance
    'pr': 5,  # pirce resistance
    'fr': 1,  # fire resistance
    'ac': 2,  # acid resistance
    **Thing(),
}
