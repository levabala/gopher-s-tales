from scripts.EventPipe import EventPipe
from scripts.areas.RootArea import RootArea
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.RoadArea import RoadArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea
from scripts.events.performable.EnterRegionEvent import EnterRegionEvent
from scripts.areas.WasteGround import WasteGroundArea

# TODO: make area possible to return different data: events, numbers etc.


def MidTownAreas(): return {
    'area name': 'Mid Town',
    'enter region': lambda w: EventPipe(w, EnterRegionEvent),
    'areas': [
        [ForestArea(), MarketArea(), ForestArea(), ForestArea()],
        [ForestArea(), HoleArea(), RoadArea(), ForestArea()],
        [WasteGroundArea(), WasteGroundArea(), RoadArea(), MarketArea()],
    ],
    ** RootArea()
}
