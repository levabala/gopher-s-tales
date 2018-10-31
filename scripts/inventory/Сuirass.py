from scripts.structures.Thing import Thing


def Сuirass(): return {
    'name': 'cuirass',
    'type': 'body armor',
    'sm': 2,  # smash resistance
    'sl': 9,  # slice resistance
    'pr': 6,  # pirce resistance
    'fr': 3,  # fire resistance
    'ac': 3,  # acid resistance
    **Thing(),
}
