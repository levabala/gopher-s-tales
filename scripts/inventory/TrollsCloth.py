from scripts.structures.Thing import Thing


def TrollsCloth(): return {
    'name': 'trolls cloth',
    'type': 'body armor',
    'weight': 0.3,
    'sm': 1,  # smash resistance
    'sl': 3,  # slice resistance
    'pr': 1,  # pirce resistance
    'fr': 7,  # fire resistance
    'ac': 8,  # acid resistance
    **Thing(),
}
