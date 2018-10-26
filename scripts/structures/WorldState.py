from collections import namedtuple

WorldState = namedtuple('WorldState', [
    'currentAreaPointer',
    'areas',
    'g',
    'yourBet',
])
