from scripts.areas.RootArea import RootArea


def RiceArea(): return {
    'area name': 'Rice',
    'symbol': '"',
    'move cost': 0,
    **RootArea()
}
