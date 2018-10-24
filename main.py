from scripts.GameCycle import runGameCycle
from scripts.structures.WorldState import WorldState
from scripts.structures.Point import Point
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea

areas = [
    [EmptyArea, MarketArea, EmptyArea],
    [EmptyArea, HoleArea, EmptyArea],
    [EmptyArea, EmptyArea, EmptyArea],
]

world = WorldState(
    currentArea=Point(x=1, y=1),
    areas=areas,
)

runGameCycle(world)
