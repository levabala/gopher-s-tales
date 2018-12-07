from scripts.structures.Thing import Thing


def AwesomeArmor(): return {
    'name': 'awesome armor',
    'type': 'body armor',
    'weight': 0.1,
    'sm': 10,  # smash resistance
    'sl': 10,  # slice resistance
    'pr': 10,  # pirce resistance
    'fr': 10,  # fire resistance
    'ac': 10,  # acid resistance
    **Thing(),
}
