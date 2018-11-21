from scripts.inventory.Сuirass import Сuirass
from scripts.inventory.Dagger import Dagger
from scripts.inventory.BlackSword import BlackSword
from scripts.inventory.Sword import Sword
from scripts.GameCycle import runGameCycle
from scripts.structures.WorldState import WorldState
from scripts.structures.Point import Point
from scripts.structures.Gopher import defaultGopher
from scripts.MapScripts import stringMapToAreas

from scripts.areas.SandArea import SandArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.TownArea import TownArea
from scripts.areas.MainTownArea import MainTownArea
from scripts.areas.SlimesArea import SlimesArea
from scripts.areas.WildWolvesArea import WildWolvesArea
from scripts.areas.FireLizardsArea import FireLizardsArea
from scripts.areas.MountainFeet import MountainFeetArea
from scripts.areas.LeftMountainArea import LeftMountainArea
from scripts.areas.RightMountainArea import RightMountainArea
from scripts.areas.WaterArea import WaterArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.MarshesArea import MarshesArea
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.VastFieldArea import VastFieldArea
from scripts.areas.GrifonesArea import GrifonesArea
from scripts.areas.FerryArea import FerryArea
from scripts.areas.CaveTrollsArea import CaveTrollsArea

topRegionAreas = [
    SandArea,
    ForestArea,
    TownArea,
    MainTownArea,
    SlimesArea,
    WildWolvesArea,
    FireLizardsArea,
    MountainFeetArea,
    LeftMountainArea,
    RightMountainArea,
    WaterArea,
    MarketArea,
    MarshesArea,
    VastFieldArea,
    GrifonesArea,
    FerryArea,
    CaveTrollsArea,
]


m = '''
    |LLLL:::::::::::::::::::::::::::::::FFFFFFFFFFF-----------------SSSSS-|
    |LLLL::::::::::::::::::::::::::::::::::FFFFFFFFF---~~~-----------SSSS-|
    |L::::::::::::::::::###########:::::::::::FFFFF------~~~~~--------SSS-|
    |###::::::::::::::##############:::::::FFFFFF---~~~~~~~~~~~~~~~~~~----|
    |:###:::########:::::#####:::::::::::::::FFF--~~~~~--------~~~~~~~--FF|
    |^:#::::::#####::^::::GGG####:::::::::FFF::::::::::FFFFFF---~~~~~--FFF|
    |^^::::::::#####^^###GGGG#############FF-~~~~-FFFFFFFFFFFF-~--~~~~---F|
    |/\^^^:::::###^^^####GGG##########FF#FFF-~~~~-FFFFFFFFFFFFFFF-----FFFF|
    |/\/\/\^^::::^/\^^####FFFFFFFFFFF########-~~~~-FFFFFFFFFFFFFFFFFFFFFFF|
    |/\/\/\/\^^:^^/\^^######FFFFF^FFFFFF####-~~~~TTTTFFFFFFFFFFFFFFFFFFFFF|
    |/\/\/\/\/\^^/\^^^###FFFFFF^^FFFFFF####-~~~~TTTQTFFFFFFFFFFFFFFFFFFFFF|
    |/\/\/\/\/\/\/\^^^##^^^FFF^^FFFFF#######-~~~~-FFFFFFFFFFFFFFFFFFFFFFFF|
    |/\/\/\/\/\/\/\/\^^^^^^^^^/\^FFF##########-~~~~-FFFFFFFFFFFFFFFFFFFFFF|
    |/\/\/\/\/\/\^CCC^^^^^^/\^^F###########-~~~~~-FFFFFFFFFFFFFFFFFFFWWWWF|
    |/\/\/\/\/\/\^CCCC^/\/\^^^FFFF####-~~~~~~~~~--FFFFFFFFFFFFFFFFFFWWWWWF|
    |/\/\/\/\/\/\/\/\/\/\/\^FF########-~~~~~~~~~~~~-FFFFFFFFFFFFFFFFWWWWWF|
'''

regions = stringMapToAreas(m, topRegionAreas)


simpleSword = Sword()
blackSword = BlackSword()
dagger = Dagger()
simpleCuirass = Сuirass()

gopher = defaultGopher('Jacob')._replace(
    inventory=[
        blackSword, simpleCuirass, dagger
    ],
    equipement=[simpleSword],
)

world = WorldState(
    locationPath=[
        Point(x=46, y=10),
    ],
    regions=regions,
    g=gopher,
    yourBet=0,
    days=0,
)

runGameCycle(world)
