from scripts.areas.ConnectedArea import ConnectedArea


def RoadArea(): return {
    'area name': 'Road',
    **ConnectedArea()
}
