from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import (
    showStory,
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
    successCritBound,
    successSimpleBound,
    failureCritChange,
    failureSimpleChange,
    successSimpleChange,
    successCritChange,
):
  showStory(textsModule.INIT)

  world = worldProcessor(world)
  d = diceFunc(world)

  if d < failureCritBound:
    smoothPrint(CRITICAL_FAILURE)
    showStory(textsModule.FAILURE_CRIT)
    return failureCritChange(world)

  elif d < failureSimpleBound:
    smoothPrint(SIMPLE_FAILURE)
    showStory(textsModule.FAILURE_SIMPLE)
    return failureSimpleChange(world)

  elif d < successSimpleBound:
    smoothPrint(SIMPLE_SUCCESS)
    showStory(textsModule.SUCCESS_SIMPLE)
    return successSimpleChange(world)

  elif d < successCritBound:
    smoothPrint(CRITICAL_SUCCESS)
    showStory(textsModule.SUCCESS_CRIT)
    return successCritChange(world)

  # should be never
  raise Exception('very strange dice')
