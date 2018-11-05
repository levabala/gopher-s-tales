from scripts.structures.Thing import Thing


def GooArmor(): return {
    'name': 'goo armor',
    'type': 'body armor',
    'weight': 0.3,
    'sm': -3,  # smash resistance
    'sl': 4,  # slice resistance
    'pr': 7,  # pirce resistance
    'fr': -6,  # fire resistance
    'ac': 9,  # acid resistance
    **Thing(),
}
