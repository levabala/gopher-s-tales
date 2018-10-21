from collections import namedtuple

FullDescription = namedtuple('FullDescription', [
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
])


def getFullDescription(target):
  return FullDescription(
      name=target.name,
      health=target.health,
      weight=target.weight,
      fame=target.fame,
      holeDeep=target.holeDeep,
      wealth=target.wealth,
      respect=target.respect,
      strenght=target.strenght,
      agility=target.agility,
      intelligence=target.intelligence,
  )
