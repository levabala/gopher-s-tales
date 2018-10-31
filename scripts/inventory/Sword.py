from scripts.structures.Thing import Thing


def Sword(): return {
    'name': 'sword',
    'type': 'weapon',
    'sm': 1,  # smash damage
    'sl': 6,  # slice damage
    'pr': 3,  # pirce damage
    'fr': 0,  # fire damage
    'ac': 0,  # acid damage
    **Thing(),
}
