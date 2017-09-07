import time
import random

__version__ = '0.0.1'

currentTime = "dawn"
starttime = time.time()
hungertime=time.time()
health = 100
damage = 15
monsterHealth=100
hungerint = 100
fire = False
deerservrint=0
deerservcint=0
firewoodint=0
inventoryarr = []
firstPrinciples = ['least privilege', 'info hiding', 'abstraction', 'simplicity', 'modularization', 'resource encapsulation', 'layering', 'process isolation', 'minimization', 'domain separation']

def main():
    intro()
    passTime()

def getPrinciple():
    return random.choice(firstPrinciples)

def intro():
    global fire
    print("")
    print("+------------------------------------------------+")
    print("| Welcome to Team 7's GenCyber RPG, version " + __version__ + ".             |")
    print("+------------------------------------------------+")
    print("")
    print("Please note that saving the game is currently unsupported.")
    print("Dawn and dusk last 30 seconds each, while day and night last 120 seconds each.")
    print("Type 'help' for help.")
    #print("you have a fire going")
    fire = False

def passTime():

    # temporarily fixed some stuff, need to do more testing.

    while True:
        timeNext()

def timeNext():

    # may or may not break passTime()

    if currentTime == "dawn":
        day()
    elif currentTime == "day":
        dusk()
    elif currentTime == "dusk":
        night()
    elif currentTime == "night":
        dawn()
    else:
        print("Unexpected time encountered. Exiting...")
        exit()

def dawn():
   
    global currentTime, starttime
    
    currentTime = "dawn"
    print("The sun is rising.")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def day():
    
    global currentTime, starttime
    
    currentTime = "day"
    print("Day has broken.")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(120.0 - ((time.time() - starttime) % 120.0))

def dusk():
    
    global currentTime, starttime
    
    currentTime = "dusk"
    print("The sun is setting.")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def night():
    global fire
    global currentTime, starttime
    global monsterHealth
    
    currentTime = "night"
    print("Night has fallen.")
    print("You feel the presence of a monster")
    monsterChance = random.randint(1,100)
    if monsterChance >= 50 and fire == False:
        # print("There are monsters out here...")
        monsterHealth=100
        battleIntro("monster")
        battleTurns("monster")
    else:
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
        hungertimeset()
        
        # time.sleep(30.0 - ((time.time() - starttime) % 30.0))
        
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def inventoryset():
    global deerservrint,deerservcint,firewoodint,inventoryarr
    pos = [deerservrint,deerservcint,firewoodint]
    strings = [" servings of raw deer", " servings of cooked deer", " stacks of firewood"]
    inventoryarr = []
    i = 2
    while i > -1:
        n = pos[i]
        if n > 0:
            n = str(n)
            strin = n + strings[i]
            inventoryarr.append(strin)
            n = int(n)
        i -= 1

def hungertimeset():
    global hungerint,hungertime
    h = time.time()
    hungertime = h - hungertime
    hungerint = hungerint-(hungertime/4)
    hungertime = h
    hungerint=int(hungerint)
    if hungerint < 20 and hungerint > 10:
        print("You're less than 20% full, find something to eat!")
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    elif hungerint < 10 and hungerint > 5:
        print("You're less than 10% full, quick - go hunting before you starve!")
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    elif hungerint < 5 and hungerint >0:
        print("You're less than 5% full, get food NOW or you'll starve!")
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    elif hungerint < 0 or hungerint == 0:
        print("You have died of hunger")
        exit()

commands = {}

def Command(func):
    commands[func.__name__] = func
    return func

def decide(user_input):
    if user_input in commands:
        return commands[user_input]()	
    else:
        print("I don't understand what you mean.")
        hungertimeset()
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))

@Command

# command functions go down here

def hunger():
    global hungerint
    hungertimeset()
    hungerstr=str(hungerint)
    print("You are " + hungerstr + "% full")
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def eat():
    global deerservrint,deerservcint,hungerint
    if deerservcint > 0:
        deerservcint -=1
        hungerint += 20
        if hungerint >100:
            hungerint = 100
            print("You are 100% full")
        else:
            hunger()
    elif deerservrint == 0 and deerservcint ==0:
        print("You don't have any deer. Go hunt for some.")
    elif deerservrint > 0 and deerservcint == 0:
        print("You have some deer, but it still needs to be cooked")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def cook():
    global deerservrint,deerservcint,fire
    if deerservrint > 0 and fire == True:
        print("You are cooking some deer...\n")
        time.sleep(2)
        deerservrint -= 1
        deerservcint += 1
        print("You have cooked 1 serving of deer")
    elif deerservrint > 0 and fire == False:
        print("You need a fire to cook your deer")
    elif deerservrint == 0:
        print("You don't have any deer to cook")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def inventory():
    inventoryset()
    global inventoryarr
    invent=str(inventoryarr)
    print("inventory: "+invent)
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def fire():
    global fire,firewoodint
    
    if fire == True:
        print("You already have a fire")
        fire = True
    elif fire == False and firewoodint > 0:
        firewoodint -= 1
        print("You have made a fire, this should keep monsters away.")
        fire = True
    elif fire == False and firewoodint == 0:
        print("You don't have any wood for a fire.\n You can forage for some though.")
    hungertimeset()
    timeIn = input(">> ")
    #time.sleep(1)
    # dark = True
    #timeIn = input(">> ")
    decide(timeIn)
    
    #time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def strength():
    global health
    print("You currently have ",health, " health")
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)

    
def forage():
    global firewoodint
    find = random.randint(0,1000)
    if find < 250:
        river()
    elif find >= 250 and find< 400:
        print("You found some berries...")
        time.sleep(1)
        print("Some berries are poisonous - will you take the risk with these?")
        eatBerries()
    elif find >= 400 and find < 750:
        print("You found some wood for a fire")
        firewoodint += 1
        hungertimeset()
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    else:
         print("You found nothing. Hard luck!")
         hungertimeset()
         timeIn = input(">> ")
         decide(timeIn)
         time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def hunt():
    global monsterHealth
    find = random.randint(0,1000)
    if find <= 400:
        monsterHealth=60
        battleIntro("animal")
        battleTurns("animal")
    elif find < 600 and find > 400:
        print("You didn't find any deer, but you found some berries...")
        time.sleep(1)
        print("Some berries are poisonous - will you eat these?")
        eatBerries()
            
    else:
         print("You couldn't find anything edible...")
         hungertimeset()
         timeIn = input(">> ")
         decide(timeIn)
         time.sleep(30.0 - ((time.time() - starttime) % 30.0))


def eatBerries():
    global hungerint
    print("yes/no")
    eat = input(">>")
    if eat == "yes":
            poison=random.randint(0,100)
            if poison < 80:
                print("You ate the berries")
                hungerint += 10
                hungertimeset()
                timeIn = input(">> ")
                decide(timeIn)
                time.sleep(30.0 - ((time.time() - starttime) % 30.0))
            elif poison > 79:
                print("Oh no!  The berries were poisonous")
                hungerint -= 5
                hungertimeset()
                timeIn = input(">> ")
                decide(timeIn)
                time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    elif eat=="no":
            print("You left the berries")
            hungertimeset()
            timeIn = input(">> ")
            decide(timeIn)
            time.sleep(30.0 - ((time.time() - starttime) % 30.0))

    else:
            print("I don't understand what you mean.")
            print("Will you eat the berries?")
            eatBerries()
    
    
def help():
    print("Commands you can use are: " + " ".join(commands.keys()))
    hungertimeset()
    timeIn = input(">> ")
    decide(timeIn)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

def watch():
    if currentTime == "dawn":
        print("You watch the sunrise.")
        time.sleep(2.5)
        timeNext()
        
    elif currentTime == "day":
        print("You watch the landscape around you.")
        time.sleep(5)
        timeNext()
        
    elif currentTime == "dusk":
        print("You watch the sunset.")
        time.sleep(2.5)
        timeNext()
        
    elif currentTime == "night":
        print("You watch the stars.")
        time.sleep(5)
        timeNext()
        
    else:
        print("You exist outside of spacetime, and simply are.")
    

def nap():   
    global fire,monsterHealth
    print("You take a brief nap.")
    #fire = not fire
    
    monsterChance = random.randint(1,100)
    if monsterChance > 75 and fire == False:
        monsterHealth=100
        battleIntro("monster")
        battleTurns("monster")
    else: 
        if fire == True:
            fire = not fire
            print("The fire burned out")
        monsterChance = 0
        timeNext()
    #if fire == True:



def river():
    global health
    print("you found a river, you can drink or leave")
    action = input(">>")
    if action == "drink":
        print("Yum, you drank some tasty water")
        health += 10
        if health > 100:
            health = 100
            print("You have 100% health and have left the river")   
            hungertimeset()
            timeIn = input(">> ")
            decide(timeIn)
            time.sleep(30.0 - ((time.time() - starttime) % 30.0))
        else:
            river()
    elif action == "leave":
        print("you left the river")
        hungertimeset()
        timeIn = input(">> ")
        decide(timeIn)
        time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    else:
        print("I don't understand what you mean. Please type drink or leave")
        river()
        
     
        
        

def battleIntro(animal_monster):
    if animal_monster=="monster":
        print()
        print("A monster approaches you!")
        print("You are in a battle with a monster!")
        print("commands are 'heal' 'attack' 'run'")
        print()
    if animal_monster=="animal":
        print()
        print("You find and sneak up on a deer!")
        print("It's a big buck with antlers, be careful!")
        print("commands are 'heal' 'attack' 'run'")
        print()

def battleTurns(animal_monster):
    global health
    global monsterHealth
    global deerservrint
    while True:
        playerAttack(animal_monster)
        monsterAttack(animal_monster)
        
        if health <= 0:
            print("You've died..")
            exit()
        if monsterHealth <= 0:
            if animal_monster=="monster":
                print("You've defeated the monster!")
                timeNext()
            if animal_monster=="animal":
                print("You've defeated the deer!")
                print("3 servings of deer have been added to your inventory...")
                deerservrint +=3
                timeNext()
            
def playerAttack(animal_monster):
    global health
    global damage
    global monsterHealth
    tripChance = random.randint(1,100)
    print("What will you do?")
    battleAction = input(">> ")
    print()
    if battleAction == "heal":
        health += 20
        if health > 100:
            health = 100
            print("you have maximum health")
        else:
            print("you healed yourself 20 points!")
        print()
    elif battleAction == "attack":
        if tripChance < 30:
            print("You tripped! You're a clumsy fool.")
            print("You lose 5 healthpoints due to embarassment.")
            health -= 5
            print()
        if tripChance >= 31:
            if animal_monster == "monster":
                prin = getPrinciple()
                print("You used the first principle of ", prin, " to deal " ,damage, "damage to the monster!")
                monsterHealth -= damage
            if animal_monster == "animal":
                prin = getPrinciple()
                print("You used the first principle of ", prin, " to deal " ,damage,  "damage to the deer!")
                monsterHealth -= damage
        print()
    elif battleAction == "run":
        if tripChance > 99:
            if animal_monster == "monster":
                print("You tripped and got hit by the monster, losing 5 health points")
                health -= 5
            if animal_monster == "animal":
                print("you tripped and got hit by the deer, losing 2 health points")
                health -= 2
            print()
        if tripChance <= 99:
            print("You have fled the scene!")
            timeIn = input(">> ")
            decide(timeIn)
            time.sleep(30.0 - ((time.time() - starttime) % 30.0))
            hungertimeset()
    else:
        print("I did not reckognize that command.\n Please type attack, heal, or run.")
        playerAttack(animal_monster)

def monsterAttack(animal_monster):
    global health
    global monsterHealth
    global hungerint
    monsterAction = random.randint(1,100)
    if monsterAction >= 0 and monsterAction < 15 and monsterHealth < 100:
        if animal_monster == "monster":
            print("The monster healed 15 health points")
            monsterHealth += 15
        if animal_monster == "animal":
            print("The deer just sat there and stared.")
        print()
    elif monsterAction > 15 and monsterAction < 40:
        if animal_monster == "monster":
            print("The monster attacked you!")
            health -= 10
        if animal_monster == "animal":
            print("The deer attacked you!")
            health -= 4
        print()
    elif monsterAction > 40 and monsterAction < 45 and monsterHealth > 0:
        if animal_monster == "monster":
            print("The monster fled the scene!")
        if animal_monster == "animal":
            print("The deer fled the scene!")
        timeNext()
    elif monsterAction > 45 and monsterAction < 65:
        if animal_monster == "monster":
            print("The monster used its heavy attack!")
            health -= 20
        if animal_monster == "animal":
            print("The deer used its heavy attack!")
            health -= 9
        print()
    elif monsterAction > 65 and monsterAction < 75:
        if animal_monster == "monster":
            print("The monster tripped trying to attack you...\nYou laugh and gain 5 health")
            health += 5
        if animal_monster == "animal":
            print("The deer tripped trying to attack you...\nYou laugh and gain 5 health")
            health += 5
        print()
    elif monsterAction > 75 and monsterAction <= 100:
        if animal_monster == "monster":
            print("The monster used its special attack!\nYou lose 20 health")
            health -= 20
        if animal_monster == "animal":
            print("The deer used its special attack!\nYou lose 10 health")
            health -= 10
        print()
    print("")
    print("+-------------------------------------------------+")
    print("   You now have", health, "health                ")
    if animal_monster == "monster":
        print("   The monster now has", monsterHealth,"health   ")
    if animal_monster == "animal":
        print("   The deer now has", monsterHealth,"health   ")
    print("+-------------------------------------------------+")
    print("")
    
# add commands here to have them work in the decision structure
commands["exit"] = exit
commands["help"] = help
commands["watch"] = watch
commands["nap"] = nap
commands["inventory"] = inventory
commands["forage"] = forage
commands["fire"] = fire
commands["strength"] = strength
commands["hunt"]=hunt
commands["hunger"]=hunger
commands["eat"] = eat
commands["cook"] = cook

# call the main function!
main()
