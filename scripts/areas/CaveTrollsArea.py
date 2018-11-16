from scripts.areas.RootArea import RootArea


def CaveTrollsArea(): return {
    'area name': 'Cave Trolls',
    'symbol': 'C',
    'move cost': 2,
    **RootArea()
}
