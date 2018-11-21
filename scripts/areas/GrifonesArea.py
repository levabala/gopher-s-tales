from scripts.areas.RootArea import RootArea
from scripts.monsters.Grifone import Grifone


def GrifonesArea(): return {
    'area name': 'Grifones',
    'symbol': 'G',
    'move cost': 1,
    'monster generate chance': 0.3,
    'monster type': Grifone,
    **RootArea()
}
