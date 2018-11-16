from scripts.areas.RootArea import RootArea


def SlimesArea(): return {
    'area name': 'Slimes',
    'symbol': 'S',
    'move cost': 2,
    **RootArea()
}
