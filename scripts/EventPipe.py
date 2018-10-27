from scripts.events.EmptyEvent import EmptyEvent


def EventPipe(world, *events):
  for event in events:
    while event != EmptyEvent and event != None:
      world, event = event(world)
  return world
