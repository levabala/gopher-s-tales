from scripts.areas.SandArea import SandArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.TownArea import TownArea
from scripts.areas.TownGateArea import TownGateArea
from scripts.areas.SlimesArea import SlimesArea
from scripts.areas.WildWolvesArea import WildWolvesArea
from scripts.areas.FireLizardsArea import FireLizardsArea
from scripts.areas.MountainFeet import MountainFeetArea
from scripts.areas.LeftMountainArea import LeftMountainArea
from scripts.areas.RightMountainArea import RightMountainArea
from scripts.areas.WaterArea import WaterArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.MarshesArea import MarshesArea
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.VastFieldArea import VastFieldArea
from scripts.areas.GrifonesArea import GrifonesArea
from scripts.areas.FerryArea import FerryArea
from scripts.areas.CaveTrollsArea import CaveTrollsArea

availableAreas = [
    SandArea,
    ForestArea,
    TownArea,
    TownGateArea,
    SlimesArea,
    WildWolvesArea,
    FireLizardsArea,
    MountainFeetArea,
    LeftMountainArea,
    RightMountainArea,
    WaterArea,
    MarketArea,
    MarshesArea,
    VastFieldArea,
    GrifonesArea,
    FerryArea,
    CaveTrollsArea,
]

areasDict = {a()['symbol']: a for a in availableAreas}


def stringMapToAreas(m):
  lines = [l.strip() for l in m.split('\n') if len(l) > 0]
  areas = []
  for line in lines:
    mapLine = line.split('|')[1]
    areasInLine = [areasDict[a]() if a in areasDict else EmptyArea() for a in mapLine]
    areas.append(areasInLine)
  return areas
