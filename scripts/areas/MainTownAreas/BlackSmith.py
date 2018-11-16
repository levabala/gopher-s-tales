from scripts.areas.RootArea import RootArea


def BlackSmithArea(): return {
    'area name': 'Black Smith',
    'symbol': 'B',
    'move cost': 0,
    **RootArea()
}
