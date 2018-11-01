from copy import deepcopy
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import (
    showStory,
    showChangedProps,
    CRITICAL_FAILURE,
    CRITICAL_SUCCESS,
    SIMPLE_FAILURE,
    SIMPLE_SUCCESS
)
from texts.events import FloodTexts, DownfallTexts, TradeTexts


def EventTrivialFunc(
    world,
    textsModule,
    changeFunc,
):
  showStory(textsModule.DESCRIBE)
  return changeFunc(world)


def EventFunc(
    world,
    worldProcessor,
    textsModule,
    diceFunc,

    failureCritBound,
    failureSimpleBound,
    successSimpleBound,
    successCritBound,

    failureCritChange,
    failureSimpleChange,
    successSimpleChange,
    successCritChange,

    afterEventAction=lambda w: w,
    showChangedPropsAfterAll=False
):
  showStory(textsModule.INIT)

  world = worldProcessor(world)
  d = diceFunc(world)

  gopherBefore = deepcopy(world.g)

  tuplya = None
  if d < failureCritBound:
    smoothPrint(CRITICAL_FAILURE)
    showStory(textsModule.FAILURE_CRIT)
    tuplya = failureCritChange(world)

  elif d < failureSimpleBound:
    smoothPrint(SIMPLE_FAILURE)
    showStory(textsModule.FAILURE_SIMPLE)
    tuplya = failureSimpleChange(world)

  elif d < successSimpleBound:
    smoothPrint(SIMPLE_SUCCESS)
    showStory(textsModule.SUCCESS_SIMPLE)
    tuplya = successSimpleChange(world)

  elif d < successCritBound:
    smoothPrint(CRITICAL_SUCCESS)
    showStory(textsModule.SUCCESS_CRIT)
    tuplya = successCritChange(world)

  else:
    # should be never
    raise Exception('very strange dice')

  tuplya = (afterEventAction(tuplya[0]), tuplya[1])

  if showChangedPropsAfterAll:
    showChangedProps(gopherBefore, tuplya[0].g)

  return tuplya
