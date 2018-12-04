from scripts.areas.RootArea import RootArea
from scripts.monsters.SlugMonster import SlugMonster
from scripts.areas.MonstersArea import MonstersArea


def SlimesArea(): return {
    'area name': 'Slimes',
    'symbol': 'S',
    'move cost': 2,
    'monster generate chance': 0.3,
    'monster type': SlugMonster,
    **RootArea(),
    **MonstersArea(),
}
