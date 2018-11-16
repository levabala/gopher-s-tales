from scripts.areas.RootArea import RootArea


def FireLizardsArea(): return {
    'area name': 'Fire Lizards',
    'symbol': 'L',
    'move cost': 2,
    **RootArea()
}
