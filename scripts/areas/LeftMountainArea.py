from scripts.areas.RootArea import RootArea


def LeftMountainArea(): return {
    'area name': 'Mountain',
    'symbol': '/',
    **RootArea()
}
