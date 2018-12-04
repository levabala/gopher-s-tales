from scripts.areas.RootArea import RootArea


def MountainFeetArea(): return {
    'area name': 'Mountain Feet',
    'symbol': '^',
    'move cost': 5,
    **RootArea()
}
