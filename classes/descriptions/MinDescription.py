from collections import namedtuple

MinDescription = namedtuple('MinDescription', [
    'name',
    'health',
    'weight',
])


def getMinDescription(target):
  return MinDescription(
      name=target.name,
      health=target.health,
      weight=target.weight,
  )
