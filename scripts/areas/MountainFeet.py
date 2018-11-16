from scripts.areas.RootArea import RootArea


def MountainFeetArea(): return {
    'area name': 'Mountain Feet',
    'symbol': '^',
    'unwalkable': True,
    'move cost': 5,
    **RootArea()
}
