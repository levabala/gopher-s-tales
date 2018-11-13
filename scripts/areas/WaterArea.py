from scripts.areas.RootArea import RootArea


def WaterArea(): return {
    'area name': 'Water',
    'symbol': '~',
    **RootArea()
}
