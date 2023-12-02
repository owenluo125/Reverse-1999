# import the random number generator
from random import uniform


# random variables
pityRate = 999
pity = 0

# unit rates
sixStarRate = [0.75/11 + 1.25*pityRate/11] # twelve 6 star units, one rate up
boostedSixStarRate = [0.75 + 1.25*pityRate] # rate up unit
boostedSixStar = "Pickles"
fiveStarRate = [4.25/10 - 8.5/98.5*2.5*pityRate/12] # twelve 5 star units, two rate up
boostedFiveStarRate = [4.25/2 - 8.5/98.5*2.5*pityRate/12] # rate up units
newFiveStar = "Diggers"
fourStarRate = [40/15 - 40/98.5*2.5*pityRate/15] # fifteen 4 star units
threeStarRate = [45/10 - 45/98.5*2.5*pityRate/10] # ten 3 star units
twoStarRate = [5/2 - 5/98.5*2.5*pityRate/2] # two 2 star units



# unit pool
unitPool = {
  "★★★★★★ " + boostedSixStar + " ★★★★★★" : boostedSixStarRate[0],
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
  "★★★★★ " + newFiveStar : boostedFiveStarRate[0],
  "★★★★★ X" : boostedFiveStarRate[0],
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

print(sum(unitPool.values()))

# randomly generate a number from 0 to around 100
unit = uniform(0, sum(unitPool.values()))

# go through all units in the pool
for x, y in unitPool.items():
  # if this has the same chance as the randomly generated unit
  if unit - y <= 0:
    # print out the unit
    print(x)
    break
  else:
    # otherwise, decrease the value of the randomly generated unit and continue
    unit -= y

  # check what rarity the unit is
