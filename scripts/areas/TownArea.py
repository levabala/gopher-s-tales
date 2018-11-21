from scripts.areas.RootArea import RootArea


def TownArea(): return {
    'area name': 'Town',
    'symbol': 'T',
    'move cost': 5,
    **RootArea()
}
