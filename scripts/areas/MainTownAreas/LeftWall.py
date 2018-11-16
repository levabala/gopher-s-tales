from scripts.areas.RootArea import RootArea


def LeftWallArea(): return {
    'area name': 'Left wall',
    'symbol': '[',
    'move cost': 0,
    'unwalkable': True,
    **RootArea()
}
