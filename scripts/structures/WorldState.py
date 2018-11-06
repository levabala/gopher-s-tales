from collections import namedtuple
from scripts.structures.Point import Point

WorldState = namedtuple('WorldState', [
    'currentAreaPointer',
    'currentRegionPointer',
    'regions',
    'g',
    'yourBet',
    'enemyType',
    'enemyState',
    'attackPoints',
    'attackerName',
    'attackerState',
    'targetState',
    'moveDelta',
    'days',
    'itemSwitchIndex',
    'arenaLevel',
])

WorldState.__new__.__defaults__ = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    0,
    None,
    0,
)
