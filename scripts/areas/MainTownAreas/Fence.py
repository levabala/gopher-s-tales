from scripts.areas.RootArea import RootArea


def FenceArea(): return {
    'area name': 'Fence',
    'symbol': '0',
    'move cost': 0,
    **RootArea()
}
