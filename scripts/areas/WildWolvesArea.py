from scripts.areas.RootArea import RootArea
from scripts.areas.MonstersArea import MonstersArea
from scripts.monsters.WildWolve import WildWolve


def WildWolvesArea(): return {
    'area name': 'Wolves',
    'symbol': 'W',
    'move cost': 2,
    'monster generate chance': 0.3,
    'monster type': WildWolve,
    **RootArea(),
    **MonstersArea(),
}
