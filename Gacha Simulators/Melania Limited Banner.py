import random

sixStarRate = [68181818] # 12 (missing 2)
boostedSixStarRate = [750000000]
fiveStarRate = [472222222] # 11 (missing 2)
boostedFiveStarRate = [2125000000]
fourStarRate = [2666666670] # 15
threeStarRate = [4500000000] # 10
twoStarRate = [2500000000] # 2

melania = 0
sweetheart = 0
balloonParty = 0

unitPool = {
  "★★★★★★ Melania ★★★★★★" : boostedSixStarRate[0],
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
  "★★★★★ Sweetheart" : boostedFiveStarRate[0],
  "★★★★★ Baby Blue" : fiveStarRate[0],
  "★★★★★ Charlie" : fiveStarRate[0],
  "★★★★★ Bkornblume" : fiveStarRate[0],
  "★★★★★ Dikke" : fiveStarRate[0],
  "★★★★★ Balloon Party" : boostedFiveStarRate[0],
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
  global melania
  global sweetheart
  global balloonParty
  global lostPity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled

  pityRate = pity - 60
  sixStarRate = [68181818 + 113636364*pityRate]
  boostedSixStarRate = [750000000 + 1250000000*pityRate]
  fiveStarRate = [472222222 - 11985336*pityRate]
  boostedFiveStarRate = [4250000000 - 53934010*pityRate]
  fourStarRate = [2666666670 - 67681900*pityRate]
  threeStarRate = [4500000000 - 114213200*pityRate]
  twoStarRate = [2500000000 - 63451780*pityRate]

  unitPool = {
    "★★★★★★ Melania ★★★★★★" : boostedSixStarRate[0],
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
    "★★★★★ Sweetheart" : boostedFiveStarRate[0],
    "★★★★★ Baby Blue" : fiveStarRate[0],
    "★★★★★ Charlie" : fiveStarRate[0],
    "★★★★★ Bkornblume" : fiveStarRate[0],
    "★★★★★ Dikke" : fiveStarRate[0],
    "★★★★★ Balloon Party" : boostedFiveStarRate[0],
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
    
    unit = random.randint(1, 99999999996 + pityRate*10)
    originalUnit = unit

    if unit <= (1499999998 + 2500000000*pityRate):
      sixPulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8499999998 - 215736040*pityRate):
      fivePulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8499999998 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate):
      fourPulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8499999998 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate) + (45000000000 - 1142132000*pityRate):
      threePulled += 1
    elif unit <= (1499999998 + 2500000000*pityRate) + (8499999998 - 215736040*pityRate) + (40000000000 - 1015228400*pityRate) + (45000000000 - 1142132000*pityRate) + (5000000000 - 126903550*pityRate):
      twoPulled += 1
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        if x == "★★★★★ Sweetheart":
          sweetheart += 1
        elif x == "★★★★★ Balloon Party":
          balloonParty += 1
        if originalUnit <= 1499999998 + 2500000000*pityRate and lostPity > 0:
          print("★★★★★★ Melania ★★★★★★")
          lostPity = 0
          melania += 1
          x = "★★★★★★ Melania ★★★★★★"   
        else:
          print(x)
        if originalUnit <= 1499999998 + 2500000000*pityRate:
          pity = 0
          if x != "★★★★★★ Melania ★★★★★★":
            lostPity += 1
        break
  else:
    sixPulled += 1
    pity = 0
    pityUnit = random.randint(1,22)
    if pityUnit > 11: # melania
      lostPity = 0
      melania += 1
      print("★★★★★★ Melania ★★★★★★")
    elif lostPity > 0:
      lostPity = 0
      melania += 1
      print("★★★★★★ Melania ★★★★★★")
    else:
      lostPity += 1
      print(random.choice(list(unitPool)[1:12]))





def pull():
  global totalPulls
  global pity
  global melania
  global sweetheart
  global balloonParty
  global lostPity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled

  for x in range(pulls):
    unit = random.randint(1, 99999999996)
    originalUnit = unit
    totalPulls += 1
    if pity >= 60:
      pitySystem()
      continue
    elif unit <= 1499999998:
      sixPulled += 1
      pity = 0
    elif unit <= 9999999996:
      fivePulled += 1
      pity += 1
    elif unit <= 49999999996:
      fourPulled += 1
      pity += 1
    elif unit <= 94999999996:
      threePulled += 1
      pity += 1
    else:
      twoPulled += 1
      pity += 1
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        if lostPity > 0 and originalUnit <= 1499999998:
          print("★★★★★★ Melania ★★★★★★")
          x = "★★★★★★ Melania ★★★★★★"
          lostPity = 0
        elif lostPity == 0 and originalUnit <= 1499999998:
          lostPity += 1
          print(x)
        else:
          print(x)
        if x == "★★★★★★ Melania ★★★★★★":
          melania += 1
        elif x == "★★★★★ Sweetheart":
          sweetheart += 1
        elif x == "★★★★★ Balloon Party":
          balloonParty += 1
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
  print("Melania: " + str(melania))
  print("Sweetheart: " + str(sweetheart))
  print("Balloon Party: " + str(balloonParty))
  print("_______________________________________")
