from toolz.functoolz import pipe
from copy import deepcopy
from classes.Event import __EventTrivialFunc__
from classes.events import WeekTaxEvent
from classes.Constants import *
from classes.GopherVisual import smoothPrint
from texts.events import StartDayTexts


def StartDayEvent(rt):
  return __EventTrivialFunc__(
      rt,
      StartDayTexts,
      lambda rt: pipe(rt, startDay)
  )


def startDay(rt):
  smoothPrint('\n--- Day {} ---\n'.format(rt.w.totalDays), BIG_DELAY)
  gopherState = deepcopy(rt.g)

  return rt._replace(w=rt.w._replace(gopherAfterNight=gopherState))
