import random

sixStarRate = [68181818] # 12 (missing 2)
boostedSixStarRate = [750000000]
fiveStarRate = [425000000] # 12
boostedFiveStarRate = [2125000000]
fourStarRate = [2666666670] # 15
threeStarRate = [4500000000] # 10
twoStarRate = [2500000000] # 2

pickles = 0
diggers = 0
babyBlue = 0

unitPool = {
  "★★★★★★ Pickles ★★★★★★" : boostedSixStarRate[0],
  "★★★★★★ Druvis III ★★★★★★" : sixStarRate[0],
  "★★★★★★ Lilya ★★★★★★" : sixStarRate[0],
  "★★★★★★ A Knight ★★★★★★" : sixStarRate[0],
  "★★★★★★ Sotheby ★★★★★★" : sixStarRate[0],
  "★★★★★★ Regulus ★★★★★★" : sixStarRate[0],
  "★★★★★★ Centurion ★★★★★★" : sixStarRate[0],
  "★★★★★★ An-an Lee ★★★★★★" : sixStarRate[0],
  "★★★★★★ Medicine Pocket ★★★★★★" : sixStarRate[0],
  "★★★★★★ Eternity ★★★★★★" : sixStarRate[0],
  "★★★★★★ Ms. NewBabel ★★★★★★" : sixStarRate[0],
  "★★★★★★ Voyager ★★★★★★" : sixStarRate[0],
  "★★★★★ X" : fiveStarRate[0],
  "★★★★★ Diggers" : boostedFiveStarRate[0],
  "★★★★★ Sweetheart" : fiveStarRate[0],
  "★★★★★ Baby Blue" : fiveStarRate[0],
  "★★★★★ Charlie" : fiveStarRate[0],
  "★★★★★ Bkornblume" : fiveStarRate[0],
  "★★★★★ Dikke" : fiveStarRate[0],
  "★★★★★ Balloon Party" : fiveStarRate[0],
  "★★★★★ Necrologist" : fiveStarRate[0],
  "★★★★★ Satsuki" : fiveStarRate[0],
  "★★★★★ Tennant" : fiveStarRate[0],
  "★★★★★ Click" : fiveStarRate[0],
  "★★★★ Nick Bottom" : fourStarRate[0],
  "★★★★ Eagle" : fourStarRate[0],
  "★★★★ Зима" : fourStarRate[0],
  "★★★★ Bunny Bunny" : fourStarRate[0],
  "★★★★ Pavia" : fourStarRate[0],
  "★★★★ Oliver Fog" : fourStarRate[0],
  "★★★★ Mondlicht" : fourStarRate[0],
  "★★★★ APPLe" : fourStarRate[0],
  "★★★★ Cristallo" : fourStarRate[0],
  "★★★★ Rabies" : fourStarRate[0],
  "★★★★ Ms. Moissan" : fourStarRate[0],
  "★★★★ Poltergeist" : fourStarRate[0],
  "★★★★ Mesmer Jr." : fourStarRate[0],
  "★★★★ Erick" : fourStarRate[0],
  "★★★★ TTT" : fourStarRate[0],
  "★★★ The Fool" : threeStarRate[0],
  "★★★ La Source" : threeStarRate[0],
  "★★★ aliEn T" : threeStarRate[0],
  "★★★ Leilani" : threeStarRate[0],
  "★★★ John Titor" : threeStarRate[0],
  "★★★ Twins Sleep" : threeStarRate[0],
  "★★★ Bette" : threeStarRate[0],
  "★★★ Darley Clatter" : threeStarRate[0],
  "★★★ ONiON" : threeStarRate[0],
  "★★★ Sputnik" : threeStarRate[0],
  "★★ Ms. Radio" : twoStarRate[0],
  "★★ Door" : twoStarRate[0]
}

totalPulls = 0
pity = 0
lostPity = 0
sixPulled = 0
fivePulled = 0
fourPulled = 0
threePulled = 0
twoPulled = 0


def pitySystem():
  global pity
  global pickles
  global diggers
  global babyBlue
  global lostPity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled

  pityRate = pity - 60
  sixStarRate = [68181818 + 113636364*pityRate]
  boostedSixStarRate = [750000000 + 1250000000*pityRate]
  fiveStarRate = [425000000 - 10786802*pityRate]
  boostedFiveStarRate = [4250000000 - 53934010*pityRate]
  fourStarRate = [2666666670 - 67681900*pityRate]
  threeStarRate = [4500000000 - 114213200*pityRate]
  twoStarRate = [2500000000 - 63451780*pityRate]

  unitPool = {
    "★★★★★★ Pickles ★★★★★★" : boostedSixStarRate[0],
    "★★★★★★ Druvis III ★★★★★★" : sixStarRate[0],
    "★★★★★★ Lilya ★★★★★★" : sixStarRate[0],
    "★★★★★★ A Knight ★★★★★★" : sixStarRate[0],
    "★★★★★★ Sotheby ★★★★★★" : sixStarRate[0],
    "★★★★★★ Regulus ★★★★★★" : sixStarRate[0],
    "★★★★★★ Centurion ★★★★★★" : sixStarRate[0],
    "★★★★★★ An-an Lee ★★★★★★" : sixStarRate[0],
    "★★★★★★ Medicine Pocket ★★★★★★" : sixStarRate[0],
    "★★★★★★ Eternity ★★★★★★" : sixStarRate[0],
    "★★★★★★ Ms. NewBabel ★★★★★★" : sixStarRate[0],
    "★★★★★★ Voyager ★★★★★★" : sixStarRate[0],
    "★★★★★ X" : fiveStarRate[0],
    "★★★★★ Sweetheart" : fiveStarRate[0],
    "★★★★★ Diggers" : boostedFiveStarRate[0],
    "★★★★★ Baby Blue" : boostedFiveStarRate[0],
    "★★★★★ Charlie" : fiveStarRate[0],
    "★★★★★ Bkornblume" : fiveStarRate[0],
    "★★★★★ Dikke" : fiveStarRate[0],
    "★★★★★ Balloon Party" : fiveStarRate[0],
    "★★★★★ Necrologist" : fiveStarRate[0],
    "★★★★★ Satsuki" : fiveStarRate[0],
    "★★★★★ Tennant" : fiveStarRate[0],
    "★★★★★ Click" : fiveStarRate[0],
    "★★★★ Nick Bottom" : fourStarRate[0],
    "★★★★ Eagle" : fourStarRate[0],
    "★★★★ Зима" : fourStarRate[0],
    "★★★★ Bunny Bunny" : fourStarRate[0],
    "★★★★ Pavia" : fourStarRate[0],
    "★★★★ Oliver Fog" : fourStarRate[0],
    "★★★★ Mondlicht" : fourStarRate[0],
    "★★★★ APPLe" : fourStarRate[0],
    "★★★★ Cristallo" : fourStarRate[0],
    "★★★★ Rabies" : fourStarRate[0],
    "★★★★ Ms. Moissan" : fourStarRate[0],
    "★★★★ Poltergeist" : fourStarRate[0],
    "★★★★ Mesmer Jr." : fourStarRate[0],
    "★★★★ Erick" : fourStarRate[0],
    "★★★★ TTT" : fourStarRate[0],
    "★★★ The Fool" : threeStarRate[0],
    "★★★ La Source" : threeStarRate[0],
    "★★★ aliEn T" : threeStarRate[0],
    "★★★ Leilani" : threeStarRate[0],
    "★★★ John Titor" : threeStarRate[0],
    "★★★ Twins Sleep" : threeStarRate[0],
    "★★★ Bette" : threeStarRate[0],
    "★★★ Darley Clatter" : threeStarRate[0],
    "★★★ ONiON" : threeStarRate[0],
    "★★★ Sputnik" : threeStarRate[0],
    "★★ Ms. Radio" : twoStarRate[0],
    "★★ Door" : twoStarRate[0]
  }

  pity += 1

  if pity < 70:

    unit = random.randint(1, 99999999998 + pityRate*10)
    originalUnit = unit

    if unit <= (1499999998 + 2500000000*pityRate):
      sixPulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8500000000 - 215736040*pityRate):
      fivePulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8500000000 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate):
      fourPulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8500000000 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate) + (45000000000 - 1142132000*pityRate):
      threePulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8500000000 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate) + (45000000000 - 1142132000*pityRate) + (5000000000 - 126903550*pityRate):
      twoPulled += 1
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        if x == "★★★★★ Diggers":
          diggers += 1
        elif x == "★★★★★ Baby Blue":
          babyBlue += 1
        if originalUnit <= 1499999998 + 2500000000*pityRate and lostPity > 0:
          print("★★★★★★ Pickles ★★★★★★")
          lostPity = 0
          x = "★★★★★★ Pickles ★★★★★★"
        else:
          print(x)
        if originalUnit <= 1499999998 + 2500000000*pityRate:
          pity = 0
          if x != "★★★★★★ Pickles ★★★★★★":
            lostPity += 1
          else:
            pickles += 1
        break
  else:
    sixPulled += 1
    pity = 0
    pityUnit = random.randint(1,22)
    if pityUnit > 11: # pickles
      lostPity = 0
      pickles += 1
      print("★★★★★★ Pickles ★★★★★★")
    elif lostPity > 0:
      lostPity = 0
      pickles += 1
      print("★★★★★★ Pickles ★★★★★★")
    else:
      lostPity += 1
      print(random.choice(list(unitPool)[1:12]))





def pull():
  global totalPulls
  global pity
  global pickles
  global diggers
  global babyBlue
  global lostPity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled

  for x in range(pulls):
    unit = random.randint(1, 99999999998)
    originalUnit = unit
    totalPulls += 1
    if pity >= 60:
      pitySystem()
      continue
    elif unit <= 1499999998:
      sixPulled += 1
      pity = 0
    elif unit <= 9999999998:
      fivePulled += 1
      pity += 1
    elif unit <= 49999999998:
      fourPulled += 1
      pity += 1
    elif unit <= 94999999998:
      threePulled += 1
      pity += 1
    else:
      twoPulled += 1
      pity += 1
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        if lostPity > 0 and originalUnit <= 1499999998:
          print("★★★★★★ Pickles ★★★★★★")
          x = "★★★★★★ Pickles ★★★★★★"
          lostPity = 0
        elif lostPity == 0 and originalUnit <= 1499999998:
          lostPity += 1
          print(x)
        else:
          print(x)
        if x == "★★★★★★ Pickles ★★★★★★":
          pickles += 1
        elif x == "★★★★★ Diggers":
          diggers += 1
        elif x == "★★★★★ Baby Blue":
          babyBlue += 1
        break

while True:
  pulls = int(input("How many pulls?  "))
  print("")
  pull()
  print()
  print("Total pulls: " + str(totalPulls))
  print("★★★★★★: " + str(sixPulled) + "(" + str(round(sixPulled*100/totalPulls, 2)) + "%)")
  print("★★★★★: " + str(fivePulled) + "(" + str(round(fivePulled*100/totalPulls, 2)) + "%)")
  print("★★★★: " + str(fourPulled) + "(" + str(round(fourPulled*100/totalPulls, 2)) + "%)")
  print("★★★: " + str(threePulled) + "(" + str(round(threePulled*100/totalPulls, 2)) + "%)")
  print("★★: " + str(twoPulled) + "(" + str(round(twoPulled*100/totalPulls, 2)) + "%)")
  print("Pickles: " + str(pickles))
  print("Diggers: " + str(diggers))
  print("Baby Blue: " + str(babyBlue))
  print("_______________________________________")
