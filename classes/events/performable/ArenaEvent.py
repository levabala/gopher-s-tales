from classes.Event import __EventTrivialFunc__
from texts.events import ArenaTexts
from classes.Constants import *
from classes.GopherMethods import calcRespect


def ArenaEvent(rt):
  return __EventTrivialFunc__(
      rt,
      ArenaTexts,
      enterArena
  )


def enterArena(rt):

  return rt
