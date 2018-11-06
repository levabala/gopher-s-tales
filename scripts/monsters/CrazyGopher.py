import texts.monsters.CrazyGopherTexts as CrazyGopherTexts
from scripts.monsters.Monster import Monster

from scripts.inventory.LeatherArmor import LeatherArmor
from scripts.inventory.RustSword import RustSword


HEALTH_POINTS = 0.5
EVASION_POINTS = 0.1
FIGHTING_LEVEL = 7

CrazyGopher = Monster(
    CrazyGopherTexts,
    HEALTH_POINTS,
    EVASION_POINTS,
    FIGHTING_LEVEL,
    [LeatherArmor, RustSword]
)
