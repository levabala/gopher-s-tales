from scripts.areas.RootArea import RootArea


def EmptyArea(): return {
    'area name': 'None',
    'symbol': 'N',
    'unwalkable': True,
    **RootArea()
}
