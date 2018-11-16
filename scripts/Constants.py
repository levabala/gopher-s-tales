from infinity import inf

SMALL_DELAY = 0.03
MEDIUM_DELAY = 0.1
BIG_DELAY = 0.6

AFTER_SLEEP_ACTION_POINTS = 3

RESPECT_A_COEFF = 1
RESPECT_B_COEFF = 1

DIG_INTELLIGENCE_COEFF = 1
DIG_STRENGTH_COEFF = 1

MAX_STAMINA = 200

# start values
START_WEALTH = 0.3

# levels
LEVEL_DIGGING_COEFF = 1
LEVEL_FIGHTING_COEFF = 1
LEVEL_TRADING_COEFF = 1

# digging
DIGGING_EVENT_FAILURE_CRIT_BOUND = 5
DIGGING_EVENT_FAILURE_SIMPLE_BOUND = 14
DIGGING_EVENT_SUCCESS_SIMPLE_BOUND = 24

DIGGING_NORMAL_DEEP = 0.1
DIGGING_WEIGHT_COST = 0.1

# flood
FLOOD_EVENT_FAILURE_CRIT_BOUND = 12
FLOOD_EVENT_FAILURE_SIMPLE_BOUND = 19
FLOOD_EVENT_SUCCESS_SIMPLE_BOUND = 30

FLOOD_EVENT_ESCAPE_COEFF = 10
FLOOD_EVENT_CRIT_HOLE_REDUCTION = 0.3
FLOOD_EVENT_SIMPLE_HOLE_REDUCTION = 0.3

# downfall
DOWNFALL_EVENT_FAILURE_CRIT_BOUND = 12
DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND = 19
DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND = 30

DOWNFALL_EVENT_ESCAPE_COEFF = 10
DOWNFALL_EVENT_CRIT_HOLE_REDUCTION = 0.3
DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE = 0.3
DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE = 0.05
DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION = 0.3

# about money
WEEK_TAX = 0.1

# trading
TRADE_EVENT_FAILURE_CRIT_BOUND = 7
TRADE_EVENT_FAILURE_SIMPLE_BOUND = 12
TRADE_EVENT_SUCCESS_SIMPLE_BOUND = 23
TRADE_EVENT_SUCCESS_CRIT_BOUND = 25

# enemy description
MIN_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND = 4
MEDIUM_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND = 8
FULL_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND = 10

# consider bounds
CONSIDER_MIN_BOUND = 4
CONSIDER_MEDIUM_BOUND = 8
CONSIDER_FULL_BOUND = 10

# attack coeffs
LIGHT_DAMAGE_COEFF = 0.2
FULL_DAMAGE_COEFF = 1
CRIT_DAMAGE_COEFF = 1.5
STRONG_ATTACK_EVASION_COEFF = 1.2
STRONG_ATTACK_DAMAGE_COEFF = 1.75
STRONG_ATTACK_WEAPON_WEIGHT_COEFF = 1.5

# evasion coeffs
MISS_DAMAGE_EVASION_COEFF = 0.8
LIGHT_DAMAGE_EVASION_COEFF = 1
FULL_DAMAGE_EVASION_COEFF = 2
CRIT_DAMAGE_EVASION_COEFF = inf

# other
YOU_STRING = 'you'
MONSTER_STRING = 'monster'
UNFRIENDLY_GOPHER_STRING = 'hostile gopher'

# sleep changes
SLEEP_CHANGES = {
    'health': 0.2,
    'weight': -0.1,
    'fame': -0.05,
    'holeDeep': -0.05,
    'stamina': 150,
}

BAD_SLEEP_CHANGES = {
    'health': 0.05,
    'weight': -0.2,
    'fame': -0.08,
    'holeDeep': -0.04,
    'stamina': 100,
}

# hold
HOLD_DURATION = 2
HOLD_EVASION_COEFF = 1.7

# escape
ESCAPE_BASE_CHANCE = 0.7
ESCAPE_FAIL_DAMAGE = 0.2
