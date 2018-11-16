from scripts.areas.RootArea import RootArea


def LeftBuildingWallArea(): return {
    'area name': 'Left building wall',
    'symbol': '/',
    'move cost': 0,
    'unwalkable': True,
    **RootArea()
}
