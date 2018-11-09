import texts.monsters.SlugTexts as TEXT_MODULE
from scripts.monsters.Monster import Monster

from scripts.inventory.GooArmor import GooArmor
from scripts.inventory.GooSlap import GooSlap


HEALTH_POINTS = 0.3
EVASION_POINTS = 0.07
FIGHTING_LEVEL = 5

SlugMonster = Monster(
    TEXT_MODULE,
    HEALTH_POINTS,
    EVASION_POINTS,
    FIGHTING_LEVEL,
    [GooArmor, GooSlap]
)
