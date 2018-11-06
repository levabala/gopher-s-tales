from scripts.structures.Thing import Thing


def LeatherArmor(): return {
    'name': 'leather armor',
    'type': 'body armor',
    'weight': 0.4,
    'sm': 4,  # smash resistance
    'sl': 2,  # slice resistance
    'pr': 2,  # pirce resistance
    'fr': 6,  # fire resistance
    'ac': 6,  # acid resistance
    **Thing(),
}
