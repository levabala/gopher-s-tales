from scripts.areas.RootArea import RootArea


def FerryArea(): return {
    'area name': 'Old Ferry',
    'symbol': '@',
    'move cost': 0,
    **RootArea()
}
