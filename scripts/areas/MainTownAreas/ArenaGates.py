from scripts.areas.RootArea import RootArea


def ArenaArea(): return {
    'area name': 'Arena',
    'symbol': 'A',
    'move cost': 0,
    **RootArea()
}
