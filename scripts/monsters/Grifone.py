import texts.monsters.GrifoneTexts as TEXT_MODULE
from scripts.monsters.Monster import Monster

from scripts.inventory.GrifonesPelt import GrifonesPelt
from scripts.inventory.GrifonClaws import GrifonClaws


HEALTH_POINTS = 0.9
EVASION_POINTS = 0.1
FIGHTING_LEVEL = 7

Grifone = Monster(
    TEXT_MODULE,
    HEALTH_POINTS,
    EVASION_POINTS,
    FIGHTING_LEVEL,
    [GrifonesPelt, GrifonClaws]
)
