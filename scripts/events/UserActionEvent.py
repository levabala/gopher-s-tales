from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import getCurrentArea
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap
from texts.events import UserActionTexts
from scripts.Completer import requestCompletableInputStrict


def UserActionEvent(w):
  return EventTrivialFunc(
      w,
      UserActionTexts,
      # we use such writing to escape circular import error
      _process
  )


def _process(w):
  while w.g.alive and w.g.stamina > 0:
    action = _getUserAction(w)

    if callable(action):
      w = action(w)
    else:
      smoothPrint(action)

    print()

  return (w, None)


def _getUserAction(w):
  area = getCurrentArea(w)

  keys = list(area.keys())

  if 'service fields' in keys:
    for field in area['service fields'] + ['areas']:
      keys.remove(field)

  actionName = requestCompletableInputStrict(
      options=keys,
      requestString='Enter action to do: ',
      wrongInputString='No such action'
  )

  return area[actionName]
