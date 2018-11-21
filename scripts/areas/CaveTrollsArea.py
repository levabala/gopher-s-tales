from scripts.areas.RootArea import RootArea
from scripts.monsters.CaveTrolls import CaveTrolls


def CaveTrollsArea(): return {
    'area name': 'Cave Trolls',
    'symbol': 'C',
    'move cost': 2,
    'monster generate chance': 0.3,
    'monster type': CaveTrolls,
    **RootArea()
}
