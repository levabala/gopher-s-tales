from scripts.areas.RootArea import RootArea


def StraightBuildingWallArea(): return {
    'area name': 'Straight building wall',
    'symbol': '|',
    'move cost': 0,
    'unwalkable': True,
    **RootArea()
}
