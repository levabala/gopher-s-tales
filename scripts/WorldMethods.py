def getArea(world, pointer):
  region = getRegion(world, world.currentRegionPointer)
  if not 'areas' in region or pointer is None:
    return region

  return region['areas'][pointer.y][pointer.x]


def getRegion(world, pointer):
  return world.regions[pointer.y][pointer.x]


def isPointerValid(world, pointer, targetMap):
  return (
      pointer.y >= 0 and pointer.y < len(targetMap) and
      pointer.x >= 0 and pointer.x < len(targetMap[0])
  )


def takeDamage(w, damage):
  return w._replace(
      targetState=w.targetState._replace(
          health=w.targetState.health - damage
      )
  )
