from scripts.areas.RootArea import RootArea


def GrifonesArea(): return {
    'area name': 'Grifones',
    'symbol': 'G',
    'move cost': 1,
    **RootArea()
}
