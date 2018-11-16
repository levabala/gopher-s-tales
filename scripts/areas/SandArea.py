from scripts.areas.RootArea import RootArea


def SandArea(): return {
    'area name': 'Sand',
    'symbol': ':',
    'move cost': 2,
    **RootArea()
}
