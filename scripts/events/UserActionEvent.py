from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import getArea
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap
from texts.events import UserActionTexts


def UserActionEvent(w):
  return EventTrivialFunc(
      w,
      UserActionTexts,
      # we use such writing to escape circular import error
      _process
  )


def _process(w):
  while w.g.actionPoints > 0 and w.g.alive:
    action = _getUserAction(w)
    w = action(w)
    print()

  return (w, None)


def _getUserAction(w):
  area = getArea(w, w.currentAreaPointer)
  # request action
  actionName = input('Enter action to do: ')
  print()

  # check for service commands
  if actionName == 'actions':
    smoothPrint('Available actions:')
    for key in area.keys():
      if callable(area[key]):
        smoothPrint('  ' + key)
    print()
    return _getUserAction(w)

  if actionName == 'my location':
    p = w.currentAreaPointer
    smoothPrint('You location: ({}, {})'.format(p.x, p.y))
    return _getUserAction(w)

  if actionName == 'show map':
    showMap(w)
    return _getUserAction(w)

  # check if action exists
  if not actionName in area:
    print('no such action!\n')
    return _getUserAction(w)
  else:
    return area[actionName]
