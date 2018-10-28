def getArea(world, pointer):
  return world.areas[pointer.y][pointer.x]


def isPointerValid(world, pointer):
  return (
      pointer.y >= 0 and pointer.y < len(world.areas) and
      pointer.x >= 0 and pointer.x < len(world.areas[0])
  )


def takeDamage(w, damage):
  return w._replace(
      targetState=w.targetState._replace(
          health=w.targetState.health - damage
      )
  )
