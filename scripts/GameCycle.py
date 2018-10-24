def runGameCycle(world,):
  cmd = ''
  areaPoint = world.currentArea
  while not cmd in world.areas[areaPoint.x][areaPoint.y]:
    cmd = input('Enter command: ')
