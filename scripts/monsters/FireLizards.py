import texts.monsters.FireLizardTexts as TEXT_MODULE
from scripts.monsters.Monster import Monster

from scripts.inventory.FireBreath import FireBreath
from scripts.inventory.LizardsScale import LizardsScale


HEALTH_POINTS = 1.5
EVASION_POINTS = 0.5
FIGHTING_LEVEL = 4

FireLizard = Monster(
    TEXT_MODULE,
    HEALTH_POINTS,
    EVASION_POINTS,
    FIGHTING_LEVEL,
    [FireBreath, LizardsScale]
)
