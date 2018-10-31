from scripts.structures.Gopher import Gopher


def isDead(gopher):
  return gopher.health <= 0 or gopher.holeDeep <= 0 or gopher.weight <= 0


def isTypeInEquipement(gopher, t):
  return any(elem['type'] != t for elem in gopher.equipement)


def equipItem(gopher, index):
  inv = gopher.inventory
  item = inv.pop(index)

  typeAlreadyExist = isTypeInEquipement(gopher, item['type'])
  if typeAlreadyExist:
    raise Exception('You can\'t equip two things of same type!')

  item['equiped'] = True

  return gopher._replace(
      inventory=inv,
      equipement=gopher.equipement + [item]
  )


def unequipItem(gopher, index):
  eqp = gopher.equipement
  item = eqp.pop(index)

  item['equiped'] = False

  return gopher._replace(
      inventory=gopher.inventory + [item],
      equipement=eqp,
  )
