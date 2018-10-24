from scripts.events.EmptyEvent import EmptyEvent


def EventPipe(world, *events):
  for event in events:
    while event != EmptyEvent:
      world, event = event(world)
  return world
