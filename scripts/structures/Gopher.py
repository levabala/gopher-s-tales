from collections import namedtuple

Gopher = namedtuple('Gopher', [
    'name',
    'health',
    'weight',
    'fame',
    'holeDeep',
    'wealth',
    'respect',
    'strenght',
    'agility',
    'intelligence',
    'charisma',
    'origin',
    'actionPoints',
    'diggingLevel',
    'fightingLevel',
    'tradingLevel',
])


def defaultGopher(name):
  return Gopher(
      name=name,
      health=1,
      weight=0.5,
      fame=0.3,
      holeDeep=0.5,
      wealth=0.5,
      respect=0.5,
      strenght=0.5,
      agility=0.5,
      intelligence=0.5,
      charisma=0.5,
      origin=None,
      actionPoints=0,
      diggingLevel=1.0,
      fightingLevel=1.0,
      tradingLevel=1.0,
  )
