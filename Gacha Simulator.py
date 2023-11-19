import random

sixStarRate = [125000000] # 12
# boostedSixStarRate = [750000000]
fiveStarRate = [772727274] # 11
# boostedFiveStarRate = [4250000000]
fourStarRate = [2666666670] # 15
threeStarRate = [4500000000] # 10
twoStarRate = [2500000000] # 2

unitPool = {
  "★★★★★★ Melania ★★★★★★" : sixStarRate[0],
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
sixPulled = 0
fivePulled = 0
fourPulled = 0
threePulled = 0
twoPulled = 0


def pitySystem():
  global pity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled
  
  pityRate = pity - 60
  sixStarRate = [125000000 + 208333333*pityRate]
  # boostedSixStarRate = [750000000]
  fiveStarRate = [772727274 - 19612370*pityRate]
  # boostedFiveStarRate = [4250000000]
  fourStarRate = [2666666670 - 67681900*pityRate]
  threeStarRate = [4500000000 - 114213200*pityRate]
  twoStarRate = [2500000000 - 63451780*pityRate]

  unitPool = {
    "★★★★★★ Melania ★★★★★★" : sixStarRate[0],
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

  if pity < 70:
    unit = random.randint(1, 100000000064)
    originalUnit = unit
    
    if unit <= (125000000 + 208333333*pityRate)*12:
      sixPulled += 1
    elif unit <= (772727274 - 19612370*pityRate)*11:
      fivePulled += 1
    elif unit <= (2666666670 - 67681900*pityRate)*15:
      fourPulled += 1
    elif unit <= (4500000000 - 114213200*pityRate)*10:
      threePulled += 1
    elif unit <= (2500000000 - 63451780*pityRate)*2:
      twoPulled += 1
    
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        print(x)
        pity += 1
        if originalUnit <= 1500000000 + 2500000000*pityRate:
          pity = 0
        break
  else:
    sixPulled += 1
    pity = 0
    print(random.choice(list(unitPool)[:12]))





def pull():
  global totalPulls
  global pity
  global sixPulled
  global fivePulled
  global fourPulled
  global threePulled
  global twoPulled
  
  for x in range(pulls):
    unit = random.randint(1, 100000000064)
    totalPulls += 1
    if pity >= 60:
      pitySystem()
      continue
    elif unit <= 1500000000:
      sixPulled += 1
      pity = 0
    elif unit <= 10000000014:
      fivePulled += 1
      pity += 1
    elif unit <= 50000000064:
      fourPulled += 1
      pity += 1
    elif unit <= 95000000064:
      threePulled += 1
      pity += 1
    else:
      twoPulled += 1
      pity += 1
    for x, y in unitPool.items():
      unit -= y
      if unit <= 0:
        print(x)
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
  print("_______________________________________")
