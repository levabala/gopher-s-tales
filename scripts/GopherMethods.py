from scripts.structures.Gopher import Gopher


def isDead(gopher):
  return gopher.health <= 0 or gopher.holeDeep <= 0 or gopher.weight <= 0


def isTypeInEquipement(gopher, t):
  return any(elem['type'] == t for elem in gopher.equipement)


def equipItem(gopher, index):
  inv = sorted(gopher.inventory, key=lambda el: el['name'])
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
  eqp = sorted(gopher.equipement, key=lambda el: el['name'])
  item = eqp.pop(index)

  item['equiped'] = False

  return gopher._replace(
      inventory=gopher.inventory + [item],
      equipement=eqp,
  )


def sumArmor(target):
  props = {
      'sm': 0,  # smashing damage
      'sl': 0,  # slicing damage
      'pr': 0,  # piercing damage
      'fr': 0,  # fire damage
      'ac': 0,  # acid damage
  }

  propsKeys = props.keys()

  for t in target.equipement:
    if 'armor' in t['type']:
      for p in propsKeys:
        props[p] += t[p]

  return props
