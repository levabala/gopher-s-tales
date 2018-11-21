from scripts.areas.RootArea import RootArea
from scripts.monsters.FireLizards import FireLizard


def FireLizardsArea(): return {
    'area name': 'Fire Lizards',
    'symbol': 'L',
    'move cost': 2,
    'monster generate chance': 0.3,
    'monster type': FireLizard,
    **RootArea()
}
