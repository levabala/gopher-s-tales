from scripts.areas.ConnectedArea import ConnectedArea


def EmptyArea(): return {
    'area name': 'None',
    **ConnectedArea()
}
