from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import UserActionTexts

# import all posible actions
from scripts.events.performable.EnterMarketEvent import EnterMarketEvent
from scripts.events.performable.DigEvent import DigEvent


def UserActionEvent(w):
  return EventTrivialFunc(
      w,
      UserActionTexts,
      # we use such writing to escape circular import error
      _process
  )


def _process(w):
  while w.g.actionPoints > 0:
    action = _getUserAction(w.currentArea)
    w = action(w)

  return (w, None)


def _getUserAction(area):
  # request action
  actionName = input('Enter action to do: ')
  print()

  # check for service commands
  if actionName == 'actions':
    print(area.keys())
    return _getUserAction(area)

  # check if action exists
  if not actionName in area:
    print('no such action!\n')
    return _getUserAction(area)
  else:
    return area[actionName]
