from scripts.areas.ConnectedArea import ConnectedArea


HoleArea = {
    'dig': lambda state: state,
    **ConnectedArea
}
