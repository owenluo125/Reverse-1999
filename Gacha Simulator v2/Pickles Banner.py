# import the random number generator
from random import uniform


# declaring variables
pityRate = 0
hardPity = 0
pity = 0
fourStarPity = 0
totalPulls = 0

# unit counter
sixStars = 0
fiveStars = 0
fourStars = 0
threeStars = 0
twoStars = 0

# new rate up units
boostedSixStar = "Pickles"
newFiveStar = "Diggers"
boostedFiveStar = "Balloon Party"
rateUpSix = 0 # rate up six star
newRateUpFive = 0 # new rate up five star
rateUpFive = 0 # existing rate up five star

while True:
  pulls = int(input("Amount of pulls: "))
  for x in range(pulls):
    totalPulls += 1
    # unit rates
    sixStarRate = [0.75/11 + 1.25*pityRate/11] # twelve 6 star units, one rate up
    boostedSixStarRate = [0.75 + 1.25*pityRate] # rate up unit
    fiveStarRate = [4.25/10 - 8.5/98.5*2.5*pityRate/12] # twelve 5 star units, two rate up
    boostedFiveStarRate = [4.25/2 - 8.5/98.5*2.5*pityRate/12] # rate up units
    fourStarRate = [40/15 - 40/98.5*2.5*pityRate/15] # fifteen 4 star units
    threeStarRate = [45/10 - 45/98.5*2.5*pityRate/10] # ten 3 star units
    twoStarRate = [5/2 - 5/98.5*2.5*pityRate/2] # two 2 star units
    
  
    # unit pool, always place boosted units at the top of the list
    # new 5 star goes at the top of 5 stars and old 5 star goes next
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
      "★★★★★ Balloon Party" : boostedFiveStarRate[0],
      "★★★★★ Sweetheart" : fiveStarRate[0],
      "★★★★★ Baby Blue" : fiveStarRate[0],
      "★★★★★ Charlie" : fiveStarRate[0],
      "★★★★★ Bkornblume" : fiveStarRate[0],
      "★★★★★ Dikke" : fiveStarRate[0],
      "★★★★★ X" : fiveStarRate[0],
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
  
    
    # randomly generate a number from 0 to around 100
    # it isn't exactly 100 since each time soft pity increases 
    # the sum has an incredibly small change, it's impossible to get it lower
    # eg. 0 soft pity has 100, 1 soft pity gets 99.99999999999999... as the sum
    if fourStarPity < 10: # almost always use this
      unit = uniform(0, sum(unitPool.values()))
    else: # if you haven't gotten a 4 star or higher after 9 pulls, you're guaranteed one
      unit = uniform(0, sixStarRate[0]*22 + fiveStarRate[0]*20 + fourStarRate[0]*15)
      
    
    # check what rarity the unit is
    if pity < 69: # if you're not at hard pity
      
      # check if it's a six star
      if unit <= sixStarRate[0]*22:
        fourStarPity = 0 # restart four star pity
        sixStars += 1 # increase count of six stars
        pity = 0 # reset pity
        if unit <= boostedSixStarRate[0] or hardPity > 0: # counter for rate up unit
          rateUpSix += 1 # increase count of rate up six stars
          hardPity = 0 # reset the 50/50
          unit = 0
        else: # if the unit is not the rate up unit
          hardPity += 1 # next unit is a guaranteed rate up
    
      # check if it's a five star
      elif unit <= sixStarRate[0]*22 + fiveStarRate[0]*20: 
        fourStarPity = 0 # restart four star pity
        fiveStars += 1 # increase count of five stars
        pity += 1 # increase pity
        if unit <= sixStarRate[0]*22 + fiveStarRate[0]*10: # counter for rate up units
          if unit <= sixStarRate[0]*22 + fiveStarRate[0]*5: # counter for new 5 star unit
            newRateUpFive += 1 # increase count of 
          else: # counter for old 5 star unit
            rateUpFive += 1
            
      # check if it's a four star
      elif unit <= sixStarRate[0]*22 + fiveStarRate[0]*20 + fourStarRate[0]*15:
        fourStarPity = 0 # restart four star pity
        fourStars += 1 # increase count of four stars
        pity += 1 # increase pity
        
      # check if it's a three star
      elif unit <= sixStarRate[0]*22 + fiveStarRate[0]*20 + fourStarRate[0]*15 + threeStarRate[0]*10:
        fourStarPity += 1 # increase four star pity
        threeStars += 1 # increase count of three stars
        pity += 1 # increase pity
    
      # if it passed all the previous checks, then it's a two star
      else:
        fourStarPity += 1 # increase four star pity
        twoStars += 1 # increase count of two stars
        pity += 1 # increase pity
      
    else: # if you're at hard pity
      sixStars += 1 # increase count of six stars
      pity = 0 # reset pity
      if hardPity > 0: # if you lost the 50/50
        unit = 0 # rate up limited unit
        rateUpSix += 1 # increase count of rate up six stars
        hardPity = 0 # reset hard pity
      else:
        unit = uniform(0, sixStarRate[0]*22) # randomly choose a six star
        if unit <= boostedSixStarRate[0]:
          rateUpSix += 1 # increase count of rate up six stars
          hardPity = 0 # reset hard pity
        else: # if the unit is not the rate up unit
          hardPity += 1 # next unit is a guaranteed rate up
        
    
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
  
    # update pity
    if pity > 60:
      pityRate = pity - 60
    else:
      pityRate = 0

  # print out the results
  print("")
  print("Total pulls: " + str(totalPulls))
  print("★★★★★★:" + str(sixStars) + "(" + str(round(sixStars*100/totalPulls, 2)) + "%)")
  print("★★★★★:" + str(fiveStars) + "(" + str(round(fiveStars*100/totalPulls, 2)) + "%)")
  print("★★★★:" + str(fourStars) + "(" + str(round(fourStars*100/totalPulls, 2)) + "%)")
  print("★★★:" + str(threeStars) + "(" + str(round(threeStars*100/totalPulls, 2)) + "%)")
  print("★★:" + str(twoStars) + "(" + str(round(twoStars*100/totalPulls, 2)) + "%)")
  print(boostedSixStar + ": " + str(rateUpSix))
  print(newFiveStar + ": " + str(newRateUpFive))
  print(boostedFiveStar + ": " + str(rateUpFive))
  print("_______________________________________")

