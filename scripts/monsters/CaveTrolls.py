import texts.monsters.CaveTrollTexts as TEXT_MODULE
from scripts.monsters.Monster import Monster

from scripts.inventory.TrollsCloth import TrollsCloth
from scripts.inventory.Hammer import Hammer


HEALTH_POINTS = 1.2
EVASION_POINTS = 0.1
FIGHTING_LEVEL = 7

CaveTrolls = Monster(
    TEXT_MODULE,
    HEALTH_POINTS,
    EVASION_POINTS,
    FIGHTING_LEVEL,
    [TrollsCloth, Hammer]
)
