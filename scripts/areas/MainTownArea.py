from scripts.EventPipe import EventPipe
from scripts.areas.RootArea import RootArea
from scripts.events.performable.EnterRegionEvent import EnterRegionEvent
from scripts.MapScripts import stringMapToAreas
from scripts.structures.Point import Point

from scripts.areas.MainTownAreas.ArenaGates import ArenaArea
from scripts.areas.MainTownAreas.BlackSmith import BlackSmithArea
from scripts.areas.MainTownAreas.Fence import FenceArea
from scripts.areas.MainTownAreas.Grass import GrassArea
from scripts.areas.MainTownAreas.Hole import HoleArea
from scripts.areas.MainTownAreas.LeftBuildingWall import LeftBuildingWallArea
from scripts.areas.MainTownAreas.LeftWall import LeftWallArea
from scripts.areas.MainTownAreas.OthersHome import OthersHomeArea
from scripts.areas.MainTownAreas.RiceGates import RiceGatesArea
from scripts.areas.MainTownAreas.RightBuildingWall import RightBuildingWallArea
from scripts.areas.MainTownAreas.RightWall import RightWallArea
from scripts.areas.MainTownAreas.StockExchange import StockExchangeArea
from scripts.areas.MainTownAreas.StraightBuildingWall import StraightBuildingWallArea
from scripts.areas.MainTownAreas.OutGates import OutGatesArea
from scripts.areas.MainTownAreas.Rice import RiceArea
from scripts.areas.WaterArea import WaterArea
from scripts.areas.SandArea import SandArea
from scripts.areas.MarshesArea import MarshesArea

from texts.areas import MAIN_TOWN_DESCRIPTIONS

mainTownAreas = [
    ArenaArea,
    BlackSmithArea,
    FenceArea,
    GrassArea,
    HoleArea,
    LeftBuildingWallArea,
    LeftWallArea,
    OthersHomeArea,
    RiceGatesArea,
    RightBuildingWallArea,
    RightWallArea,
    StockExchangeArea,
    StraightBuildingWallArea,
    OutGatesArea,
    WaterArea,
    SandArea,
    MarshesArea,
    RiceArea,
]

townString = '''
  |~~~~--[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]###|
  |~~~~-[]::::##/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\##[]#|
  |[][][]::::::#######################################################[]|
  |~~~~~:::::::#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\#/O\###[]|
  |~~~~~:::::::#######################################################[]|
  |~~~~~::::::::#############0A0########################00000000000000[]|
  |~~~~~~:::::::##########000:::000#####################0"""""""""""""[]|
  |~~~~~:::::::#########00:::::::::00###################E"""""""""""""[]|
  |~~~~~################00:::::::::00###################0"""""""""""""[]|
  |~~~~~##################000:::000#####################0"""""""""""""[]|
  |~~~~~::###################0A0########################00000000000000[]|
  |[][][]::###########################################################[]|
  |~~~~-[]::##########################################\\\\\\\\\\\\####\\\\\\\\\\\\[]|
  |~~~~--[]::#########################################B|||||####$|||||[]|
  |~~~~-::[]/H\#######################################//////####//////[]|
  |~~--::::[][][][][][][][][][]GGG[][][][][][][][][][][][][][][][][][][]|
'''


def MainTownArea(): return {
    'area name': 'Main Town',
    'symbol': 'Q',
    'enter region': lambda w: EventPipe(w, EnterRegionEvent),
    'areas': stringMapToAreas(townString, mainTownAreas),
    'move cost': 1,
    'enter point': Point(29, 15),
    'service fields': ['enter point', 'symbol'],
    'custom descriptions': MAIN_TOWN_DESCRIPTIONS,
    ** RootArea()
}
