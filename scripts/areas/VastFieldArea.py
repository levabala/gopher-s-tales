from scripts.areas.RootArea import RootArea


def VastFieldArea(): return {
    'area name': 'Vast Field',
    'symbol': '#',
    'move cost': 1,
    **RootArea()
}
