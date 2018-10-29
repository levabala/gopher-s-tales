from scripts.GameCycle import runGameCycle
from scripts.structures.WorldState import WorldState
from scripts.structures.Point import Point
from scripts.structures.Gopher import defaultGopher

from scripts.regions.MidTown import MidTownAreas

from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.RoadArea import RoadArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea


regions = [
    [ForestArea(), ForestArea(), ForestArea()],
    [ForestArea(), MidTownAreas(), ForestArea()],
    [ForestArea(), ForestArea(), ForestArea()],
]

gopher = defaultGopher('Jacob')

world = WorldState(
    currentAreaPointer=Point(x=1, y=1),
    currentRegionPointer=Point(x=1, y=1),
    regions=regions,
    g=gopher,
    yourBet=0,
)


runGameCycle(world)
