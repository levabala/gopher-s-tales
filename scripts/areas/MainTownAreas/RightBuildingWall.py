from scripts.areas.RootArea import RootArea


def RightBuildingWallArea(): return {
    'area name': 'Right building wall',
    'symbol': '\\',
    'move cost': 0,
    'unwalkable': True,
    **RootArea()
}
