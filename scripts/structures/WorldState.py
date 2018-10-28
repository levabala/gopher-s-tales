from collections import namedtuple

WorldState = namedtuple('WorldState', [
    'currentAreaPointer',
    'areas',
    'g',
    'yourBet',
    'enemyType',
    'enemyState',
    'attackPoints',
    'attackerName',
    'attackerState',
    'targetState',
])

WorldState.__new__.__defaults__ = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
)
