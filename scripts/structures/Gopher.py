from collections import namedtuple

Gopher = namedtuple('Gopher', [
    'name',
    'health',
    'weight',
    'fame',
    'holeDeep',
    'wealth',
    'respect',
    'strength',
    'agility',
    'intelligence',
    'charisma',
    'origin',
    'evasion',
    'actionPoints',
    'diggingLevel',
    'fightingLevel',
    'tradingLevel',
    'alive',
    'equipement',
    'inventory',
    'quickSlot',
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
      strength=0.5,
      agility=0.5,
      intelligence=0.5,
      charisma=0.5,
      origin=None,
      evasion=0.14,
      actionPoints=0,
      diggingLevel=1.0,
      fightingLevel=2.0,
      tradingLevel=1.0,
      alive=True,
      inventory=[],
      quickSlot=[],
      equipement=[],
  )