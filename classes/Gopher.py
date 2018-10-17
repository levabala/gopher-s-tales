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
])

# set default values
Gopher.__new__.__defaults__ = (None,) * len(Gopher._fields)


def defaultGopher(name):
  return Gopher(
      name=name,
      health=1,
      weight=0.5,
      fame=0,
      holeDeep=0.5,
      wealth=0.5,
      respect=0.5,
      strenght=0.5,
      agility=0.5,
      intelligence=0.5,
      charisma=0.5,
      origin=None,
      actionPoints=0
  )
