from classes.SmoothPrint import smoothPrint
from texts.events import FloodTexts, DownfallTexts, TradeTexts
from classes.GopherVisual import (
    CRITICAL_FAILURE,
    CRITICAL_SUCCESS,
    SIMPLE_FAILURE,
    SIMPLE_SUCCESS,
    showStory
)


def __EventTrivialFunc__(
    rt,
    textsModule,
    changeFunc,
):
  showStory(textsModule.DESCRIBE)
  return changeFunc(rt)


def __EventFunc__(
    rt,
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

  d = diceFunc(rt)

  if d < failureCritBound:
    smoothPrint(CRITICAL_FAILURE)
    showStory(textsModule.FAILURE_CRIT)
    return failureCritChange(rt)

  elif d < failureSimpleBound:
    smoothPrint(SIMPLE_FAILURE)
    showStory(textsModule.FAILURE_SIMPLE)
    return failureSimpleChange(rt)

  elif d < successSimpleBound:
    smoothPrint(SIMPLE_SUCCESS)
    showStory(textsModule.SUCCESS_SIMPLE)
    return successSimpleChange(rt)

  elif d < successCritBound:
    smoothPrint(CRITICAL_SUCCESS)
    showStory(textsModule.SUCCESS_CRIT)
    return successCritChange(rt)

  # should be never
  raise Exception('very strange dice')
