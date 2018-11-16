from scripts.areas.RootArea import RootArea


def GrassArea(): return {
    'area name': 'Grass',
    'symbol': '#',
    'move cost': 0,
    **RootArea()
}
