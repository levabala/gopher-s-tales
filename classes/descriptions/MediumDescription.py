from collections import namedtuple

MediumDescription = namedtuple('MediumDescription', [
    'name',
    'health',
    'weight',
    'fame',
    'holeDeep',
])


def getMediumDescription(target):
  return MediumDescription(
      name=target.name,
      health=target.health,
      weight=target.weight,
      fame=target.fame,
      holeDeep=target.holeDeep,
  )
