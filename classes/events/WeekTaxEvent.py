from classes.Event import __EventTrivialFunc__
from texts.events import WeekTaxTexts
from classes.Constants import *
from classes.GopherMethods import calcWeekTax


def NewDayEvent(rt):
  return __EventTrivialFunc__(
      rt,
      WeekTaxTexts,
      lambda rt: rt._replace(g=rt.g._replace(wealth=rt.g.wealth - calcWeekTax(rt.g)))
  )
