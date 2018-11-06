from random import randint
from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe
from scripts.monsters.CrazyGopher import CrazyGopher

# possible events
from scripts.events.performable.PurgeEvent import PurgeEvent

MIN_MONSTERS_COUNT = 0
MAX_MONSTERS_COUNT = 2


def WasteGroundArea(): return {
    'area name': 'Waste',
    'monsters count': randint(MIN_MONSTERS_COUNT, MAX_MONSTERS_COUNT),
    'monsters type': CrazyGopher,
    'purge': lambda w: EventPipe(w, PurgeEvent),
    **RootArea()
}
