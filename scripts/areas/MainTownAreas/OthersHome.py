from scripts.areas.RootArea import RootArea


def OthersHomeArea(): return {
    'area name': 'Other\'s home',
    'symbol': 'O',
    'move cost': 0,
    **RootArea()
}
