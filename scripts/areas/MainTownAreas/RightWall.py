from scripts.areas.RootArea import RootArea


def RightWallArea(): return {
    'area name': 'Right wall',
    'symbol': ']',
    'move cost': 0,
    'unwalkable': True,
    **RootArea()
}
