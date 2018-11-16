from scripts.areas.RootArea import RootArea


def RiceGatesArea(): return {
    'area name': 'Rice gates',
    'symbol': 'E',
    'move cost': 0,
    **RootArea()
}
