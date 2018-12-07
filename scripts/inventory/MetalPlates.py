from scripts.structures.Thing import Thing


def MetalPlates(): return {
    'name': 'metal pelt',
    'type': 'body armor',
    'weight': 0.8,
    'sm': 5,  # smash resistance
    'sl': 8,  # slice resistance
    'pr': 8,  # pirce resistance
    'fr': 4,  # fire resistance
    'ac': 2,  # acid resistance
    **Thing(),
}
