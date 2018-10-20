from classes.Event import __EventTrivialFunc__
from texts.events import SleepTexts
from classes.Constants import *
from classes.GopherMethods import calcRespect


def SleepEvent(rt):
  return __EventTrivialFunc__(
      rt,
      SleepTexts,
      lambda rt: rt._replace(
          g=rt.g._replace(
              actionPoints=AFTER_SLEEP_ACTION_POINTS,
              holeDeep=rt.g.holeDeep - 0.02,
              health=rt.g.health + 0.1,
              fame=rt.g.fame - 0.01,
              # weight=rt.g.weight - 1 / 6,
              respect=calcRespect(rt.g)
          )
      )
  )
