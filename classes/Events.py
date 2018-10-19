from classes.Assets import d20
from classes.SmoothPrint import smoothPrint
from classes.Constants import *
from texts.events import FloodTexts, DownfallTexts, TradeTexts
from classes.GopherVisual import (
    CRITICAL_FAILURE,
    CRITICAL_SUCCESS,
    SIMPLE_FAILURE,
    SIMPLE_SUCCESS,
    showStory
)


def __EventFunc__(
    gopher,
    textsModule,
    diceFunc,
    failureCritBound,
    failureSimpleBound,
    successCritBound,
    successSimpleBound,
    failureCritChange,
    failureSimpleChange,
    successCritChange,
    successSimpleChange,
):
  showStory(textsModule.INIT)

  d = diceFunc()

  if d < failureCritBound:
    smoothPrint(CRITICAL_FAILURE)
    showStory(textsModule.FAILURE_CRIT)
    return failureCritChange(gopher)

  elif d < failureSimpleBound:
    smoothPrint(SIMPLE_FAILURE)
    showStory(textsModule.FAILURE_SIMPLE)
    return failureSimpleChange(gopher)

  elif d < successSimpleBound:
    smoothPrint(SIMPLE_SUCCESS)
    showStory(textsModule.SUCCESS_SIMPLE)
    return successSimpleChange(gopher)

  elif d < successCritBound:
    smoothPrint(CRITICAL_SUCCESS)
    showStory(textsModule.SUCCESS_CRIT)
    return successCritChange(gopher)

  # should be never
  raise Exception('very strange dice')


def floodEvent(gopher):
  __EventFunc__(
      gopher,
      FloodTexts,
      lambda: d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility,
      FLOOD_EVENT_FAILURE_CRIT_BOUND,
      FLOOD_EVENT_FAILURE_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda g: g._replace(
          holeDeep=g.holeDeep - FLOOD_EVENT_CRIT_HOLE_REDUCTION,
      ),
      lambda g: g._replace(
          holeDeep=g.holeDeep - FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
      ),
      lambda g: g,
      lambda g: g,
  )


def downfallEvent(gopher):
  __EventFunc__(
      gopher,
      DownfallTexts,
      lambda: d20() + DOWNFALL_EVENT_ESCAPE_COEFF * gopher.strength,
      DOWNFALL_EVENT_FAILURE_CRIT_BOUND,
      DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda g: g._replace(
          holeDeep=gopher.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
          health=gopher.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
      ),
      lambda g: g._replace(
          holeDeep=gopher.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
          health=gopher.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
      ),
      lambda g: g,
      lambda g: g,
  )


def tradeEvent(gopher, args):
  __EventFunc__(
      gopher,
      TradeTexts,
      lambda: d20() + gopher.trading,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
      lambda g: g._replace(
          holeDeep=gopher.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
          health=gopher.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
      ),
      lambda g: g._replace(
          holeDeep=gopher.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
          health=gopher.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
      ),
      lambda g: g,
      lambda g: g,
  )
