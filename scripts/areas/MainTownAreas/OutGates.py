from scripts.areas.RootArea import RootArea


def OutGatesArea(): return {
    'area name': 'Out Gates',
    'symbol': 'G',
    'move cost': 0,
    **RootArea()
}
