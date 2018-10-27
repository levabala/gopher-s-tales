from scripts.GopherMethods import isDead
from scripts.EventPipe import EventPipe

# importing events
from scripts.events.StartGameEvent import StartGameEvent
from scripts.events.BornEvent import BornEvent
from scripts.events.StartDayEvent import StartDayEvent
from scripts.events.MidwayEvent import MidwayEvent
from scripts.events.UserActionEvent import UserActionEvent
from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.SleepEvent import SleepEvent


def runGameCycle(world):
  # Game Structure:
  #
  # StartGame (root event) ->
  # Born ->
  # StartDay ->
  # Midway ->
  # - EndDay -> StartDay
  # - Sleep -> EndDay
  # - UserAction -> Other -> Other -> Midway
  # - Dead -> FinishGame

  worldAfterEternity = EventPipe(world, StartGameEvent)

  # just to use this var
  if worldAfterEternity:
    pass
