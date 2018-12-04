from scripts.structures.Thing import Thing


def LizardsScale(): return {
    'name': 'lizards scale',
    'type': 'body armor',
    'weight': 0.5,
    'sm': 5,  # smash resistance
    'sl': 6,  # slice resistance
    'pr': 2,  # pirce resistance
    'fr': 10,  # fire resistance
    'ac': 10,  # acid resistance
    **Thing(),
}
