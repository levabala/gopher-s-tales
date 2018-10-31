from scripts.structures.Thing import Thing


def GooArmor(): return {
    'name': 'cuirass',
    'type': 'body armor',
    'sm': -3,  # smash resistance
    'sl': 4,  # slice resistance
    'pr': 7,  # pirce resistance
    'fr': -6,  # fire resistance
    'ac': 9,  # acid resistance
    **Thing(),
}
