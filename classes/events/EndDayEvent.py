from toolz.functoolz import pipe
from copy import deepcopy
from classes.Event import __EventTrivialFunc__
from classes.events import WeekTaxEvent
from classes.Constants import *
from classes.GopherVisual import smoothPrint, showChangedProps, bcolors
from classes.GopherMethods import pr2rn
from texts.events import EndDayTexts

from classes.events.performable.SleepEvent import SleepEvent


def EndDayEvent(rt):
  return __EventTrivialFunc__(
      rt,
      EndDayTexts,
      lambda rt: manageDay(rt)
  )


def manageDay(rt):
  if rt.w.weekday == 7:
    # register week tax event
    rt._replace(e=rt.e + [WeekTaxEvent])

    # reset counter
    rt._replace(w=rt.w._replace(weekday=0))

  gopherBeforeDay = rt.w.gopherAfterNight
  gopherAfterDay = deepcopy(rt.g)
  smoothPrint('{}AFTER DAY CHANGES{}'.format(bcolors.BOLD, bcolors.ENDC))
  showChangedProps(gopherBeforeDay, gopherAfterDay, ['actionPoints'])

  rt = pipe(rt, SleepEvent, pr2rn)
  gopherAfterNight = deepcopy(rt.g)
  smoothPrint('\n{}AFTER DAY&NIGHT CHANGES{}'.format(bcolors.BOLD, bcolors.ENDC))
  showChangedProps(gopherAfterDay, gopherAfterNight, ['actionPoints'])

  return rt._replace(w=rt.w._replace(weekday=rt.w.weekday + 1))
