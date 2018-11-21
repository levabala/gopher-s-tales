from scripts.structures.Point import Point


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


def forEachArea(processor, regions, path=[]):
  regionPath = path.copy()
  for y in range(len(regions)):
    for x in range(len(regions[y])):
      path = regionPath + [Point(x, y)]

      area = regions[y][x]
      if 'areas' in area:
        forEachArea(processor, area['areas'], path.copy())

      processor(area, path)


def getMonstersInLocation(w, locationPath):
  monsters = []
  for i in range(len(w.monstersInTheWorld)):
    monster = w.monstersInTheWorld[i]
    if monster.state.health <= 0:
      continue

    print('{} vs {}'.format(monster.locationPath, locationPath))
    if len(monster.locationPath) != len(locationPath):
      continue

    same = True
    for ii in range(len(monster.locationPath)):
      p1 = monster.locationPath[ii]
      p2 = locationPath[ii]
      if p1.x != p2.x or p1.y != p2.y:
        same = False
        break

    if same:
      monsters.append(monster)

  return monsters


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
