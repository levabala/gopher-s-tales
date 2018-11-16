from scripts.areas.RootArea import RootArea


def MarshesArea(): return {
    'area name': 'Marhes',
    'symbol': '-',
    'move cost': 2,
    **RootArea()
}
