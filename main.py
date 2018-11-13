from scripts.GameCycle import runGameCycle
from scripts.structures.WorldState import WorldState
from scripts.structures.Point import Point
from scripts.structures.Gopher import defaultGopher
from scripts.MapScripts import stringMapToAreas

from scripts.regions.MidTown import MidTownAreas

from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.WasteGround import WasteGroundArea
from scripts.areas.RoadArea import RoadArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea

from scripts.inventory.Sword import Sword
from scripts.inventory.BlackSword import BlackSword
from scripts.inventory.Dagger import Dagger
from scripts.inventory.Сuirass import Сuirass

m = '''
    H |LLLL:::::::::::::::::::::::::::::::FFFFFFFFFFF-----------------SSSSS-|
    I |LLLL::::::::::::::::::::::::::::::::::FFFFFFFFF---~~~-----------SSSS-|
    C |L::::::::::::::::::###########:::::::::::FFFFF------~~~~~--------SSS-|
      |###::::::::::::::##############:::::::FFFFFF---~~~~~~~~~~~~~~~~~~----|
    S |:###:::########:::::#####:::::::::::::::FFF--~~~~~--------~~~~~~~--FF|
    U |^:#::::::#####::^::::GGG####:::::::::FFF-@~~~~~@--FFFFFF---~~~~~--FFF|
    N |^^::::::::#####^^###GGGG#############FF-~~~~-FFFFFFFFFFFF-~--~~~~---F|
    T |/\^^^:::::###^^^####GGG##########FF#FFF-~~~~-FFFFFFFFFFFFFFF-----FFFF|
      |/\/\/\^^::::^/\^^####FFFFFFFFFFF########-~~~~-FFFFFFFFFFFFFFFFFFFFFFF|
    D |/\/\/\/\^^:^^/\^^######FFFFF^FFFFFF####-~~~~TTTTFFFFFFFFFFFFFFFFFFFFF|
    R |/\/\/\/\/\^^/\^^^###FFFFFF^^FFFFFF####-~~~~TTTQTFFFFFFFFFFFFFFFFFFFFF|
    A |/\/\/\/\/\/\/\^^^##^^^FFF^^FFFFF#######-~~~~-FFFFFFFFFFFFFFFFFFFFFFFF|
    C |/\/\/\/\/\/\/\/\^^^^^^^^^/\^FFF##########-~~~~-FFFFFFFFFFFFFFFFFFFFFF|
    O |/\/\/\/\/\/\^CCC^^^^^^/\^^F###########-~~~~~-FFFFFFFFFFFFFFFFFFFWWWWF|
    N |/\/\/\/\/\/\^CCCC^/\/\^^^FFFF####-~~~~~~~~~--FFFFFFFFFFFFFFFFFFWWWWWF|
    E |/\/\/\/\/\/\/\/\/\/\/\^FF########-~~~~~~~~~~~~-FFFFFFFFFFFFFFFFWWWWWF|
    S |_____________________________________________________________________|
'''

regions = stringMapToAreas(m)


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
        Point(x=0, y=0),
    ],
    regions=regions,
    g=gopher,
    yourBet=0,
    days=0,
)

runGameCycle(world)
