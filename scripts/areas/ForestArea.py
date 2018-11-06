from random import randint
from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe
from scripts.monsters.SlugMonster import SlugMonster

# possible events
from scripts.events.performable.PurgeEvent import PurgeEvent

MIN_MONSTERS_COUNT = 7
MAX_MONSTERS_COUNT = 10


def ForestArea(): return {
    'area name': 'Forest',
    'monsters count': randint(MIN_MONSTERS_COUNT, MAX_MONSTERS_COUNT),
    'monsters type': SlugMonster,
    'purge': lambda w: EventPipe(w, PurgeEvent),
    **RootArea()
}
