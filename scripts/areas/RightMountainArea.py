from scripts.areas.RootArea import RootArea


def RightMountainArea(): return {
    'area name': 'Mountain',
    'symbol': '\\',
    'unwalkable': True,
    'move cost': 5,
    **RootArea()
}