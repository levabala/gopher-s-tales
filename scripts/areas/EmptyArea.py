from scripts.areas.RootArea import RootArea


def EmptyArea(): return {
    'area name': 'None',
    **RootArea()
}
