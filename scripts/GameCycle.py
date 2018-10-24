from scripts.GopherMethods import isDead


def runGameCycle(world):
  while not isDead(world.gopher):
    world = performUserCommand(world)


def day(world):
  if isDead(world.gopher):
    print('You\'re dead!')
    return

  world =


def performUserCommand(world):
  areaPoint = world.currentArea
  area = world.areas[areaPoint.x][areaPoint.y]
  areaAfterAction = area[requestCommand(area)](world)

  return world._replace(currentArea=areaAfterAction)


def requestCommand(area):
  cmd = input('Enter action: ')
  if not cmd in area:
    print('no such action in the area')
    return requestCommand(area)

  return cmd
