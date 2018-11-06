from collections import namedtuple
from scripts.structures.Point import Point

WorldState = namedtuple('WorldState', [
    'locationPath',
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
    'holdTurnsLeft',
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
    None,
    None,
    None,
    None,
)
