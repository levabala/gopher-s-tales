from scripts.GameCycle import runGameCycle
from scripts.structures.WorldState import WorldState
from scripts.structures.Point import Point
from scripts.structures.Gopher import defaultGopher
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.RoadArea import RoadArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea

areas = [
    [ForestArea(), MarketArea(), ForestArea(), ForestArea()],
    [ForestArea(), HoleArea(), RoadArea(), ForestArea()],
    [ForestArea(), ForestArea(), RoadArea(), MarketArea()],
]

gopher = defaultGopher('Jacob')

world = WorldState(
    currentAreaPointer=Point(x=1, y=2),
    areas=areas,
    g=gopher,
    yourBet=0,
)


runGameCycle(world)
