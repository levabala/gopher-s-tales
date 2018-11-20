def getArea(world, locationPath):
  originPointer = locationPath[0]
  area = world.regions[originPointer.y][originPointer.x]

  if len(locationPath) < 2:
    return area

  for i in range(1, len(locationPath) - 1):
    pointer = locationPath[i]
    area = area['areas'][pointer.x][pointer.y]

  lastPointer = locationPath[-1]
  return area['areas'][lastPointer.y][lastPointer.x]


def getCurrentArea(world):
  return getArea(world, world.locationPath)


def forEachArea(processor, regions):
  for y in range(len(regions)):
    for x in range(len(regions[y])):
      area = regions[y][x]
      if 'areas' in area:
        forEachArea(processor, area['areas'])
      processor(area)


def getCurrentRegion(world):
  if len(world.locationPath) == 1:
    return {'areas': world.regions}
  else:
    return getArea(world, world.locationPath[:-1])


def isPointerValid(world, pointer, region):
  return (
      pointer.y >= 0 and pointer.y < len(region) and
      pointer.x >= 0 and pointer.x < len(region[0]) and
      (not 'unwalkable' in region[pointer.y][pointer.x].keys() or
       not region[pointer.y][pointer.x]['unwalkable'])
  )


def takeDamage(w, damage):
  return w._replace(
      targetState=w.targetState._replace(
          health=w.targetState.health - damage
      )
  )
