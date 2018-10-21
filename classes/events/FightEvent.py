from classes.Event import __EventTrivialFunc__
from texts.events import FightTexts
from classes.Constants import *
from classes.GopherMethods import calcRespect


def FightEvent(rt):
  return __EventTrivialFunc__(
      rt,
      FightTexts,
      do,
  )


def do(rt):
  return rt
