from scripts.areas.RootArea import RootArea


def WildWolvesArea(): return {
    'area name': 'Wolves',
    'symbol': 'W',
    'move cost': 2,
    **RootArea()
}
