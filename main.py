import time
from time import sleep
import os
import random


# Player Class
class Player():
    def __init__(self, name, level, xp, health, weapon, gold, wins, losses):
        self.name = name
        self.level = level
        self.xp = xp
        self.health = health
        self.weapon = weapon
        self.gold = gold
        self.wins = wins
        self.losses = losses


# Weapon Class
class Weapon():
    def __init__(self, name, minDmg, maxDmg, gold):
        self.name = name
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.gold = gold

    def __repr__(self):
        return "{}".format(self.name)


class Enemy():
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health


class Item():
    def __init__(self, name, gold, affect, amount):
        self.name = name
        self.gold = gold
        self.affect = affect
        self.amount = amount

    def use(self):
        if (self.affect == "health"):
            player.health += self.amount
        if (self.affect == "damage"):
            player.weapon.minDmg += self.amount
            player.weapon.maxDmg += self.amount

    def __repr__(self):
        return "{}".format(self.name)


# Weapons
dagger = Weapon("Dagger", 2, 4, 2)
sword = Weapon("Sword", 4, 8, 5)
axe = Weapon("Axe", 6, 9, 12)
fireSword = Weapon("Fire Sword", 10, 15, 20)
swordOfTheChoosen = Weapon("Sword of the Chosen", 30, 37, 80)

weaponList = [dagger, sword, axe, fireSword, swordOfTheChoosen]

# Items
healthPotion = Item("Health Potion", 1, "health", 5)
damagePotion = Item("Damage Potion", 3, "damage", 2)

itemList = [healthPotion, damagePotion]

# Get player name
name = input("What is your name, warrior?\n")

level = 1
xp = 0
health = 10
gold = 1

# Easter egg
if "lord" in name.lower():
    health += 2
    gold += 1

# Create player
player = Player(name, level, xp, health, dagger, gold, 0, 0)


# Intro
print("Your adventure begins now! Defeat monsters, level up, unlock new gear! Good luck, " + player.name + ".\n")
# sleep(5)
# print("3")
# sleep(1)
# print("2")
# sleep(1)
# print("1")
# sleep(1)

lvl_1_monsters = {"Spider": {"attack": 1, "health": 3},
                  "Goblin": {"attack": 2, "health": 6}, }

lvl_2_monsters = {"Spider": {"attack": 3, "health": 5},
                  "Goblin": {"attack": 6, "health": 10},
                  "Zombie": {"attack": 6, "health": 16}, }


os.system("clear")

playing = True
while (playing):
    # Main menu
    print("1) Fight\n2) Shop\n3) Inventory\n4) Stats\n0) Quit")

    # Get action
    action = int(input())
    os.system("clear")

    # If player chooses fight
    if (action == 1):
        # Generate level 1 monster
        if (player.level == 1):
            monster = random.choice(list(lvl_1_monsters))
            monster_health = lvl_1_monsters[monster]['health']
            monster_attack = lvl_1_monsters[monster]['attack']
        # Generate level 2 monster
        if (player.level >= 2):
            monster = random.choice(list(lvl_2_monsters))
            monster_health = lvl_2_monsters[monster]['health']
            monster_attack = lvl_2_monsters[monster]['attack']

        fighting = True
        # While fighting
        while (fighting):
            print(player.name + " (Lvl " + str(player.level) + ")\nHealth: " + str(player.health) +
                  "\n\n" + monster + "\nHealth: " + str(monster_health) + "\n")

            choice = int(input("1) Attack\n2) Run\n"))

            # If player attacks
            if (choice == 1):
                os.system("clear")

                # Attack monster
                if player.weapon != None:
                    dmgDealt = random.randint(
                        player.weapon.minDmg, player.weapon.maxDmg)
                monster_health -= dmgDealt
                print("You dealt {} damage.\n".format(dmgDealt))
                # sleep(1)

                # If monster died
                if (monster_health <= 0):
                    fighting = False
                    player.gold += 1
                    player.xp += 2
                    player.wins += 1
                    # Level up
                    if (player.xp >= 10):
                        player.xp = 0
                        player.level += 1
                        player.gold += 2
                        player.health += 5
                    print("You are victorious!\n")
                    del monster
                # Monster attacks
                else:
                    player.health -= monster_attack
                    print("You took {} damage.\n".format(monster_attack))
                    # sleep(1)

                    # If player died
                    if player.health <= 0:
                        fighting = False
                        print("You have been defeated!\n")
                        playing = False

                        del monster
            # If player runs
            else:
                fighting = False
                player.losses += 1
                os.system("clear")

    # If player chooses shop
    elif (action == 2):
        action = int(input(("1) Weapons\n2) Items\n")))

        # List weapons in shop
        if (action == 1):
            count = 1
            for weapon in weaponList:
                print(str(count) + ") " + weapon.name + " - Dmg: " + str(weapon.minDmg) + "-" + str(weapon.maxDmg) +
                      " - Cost: " + str(weapon.gold))
                count += 1
            weapon_no = int(input()) - 1
            print("0) Back")

            # If player has enough gold, buy weapon
            if (player.gold >= weaponList[weapon_no].gold):
                player.gold -= weaponList[weapon_no].gold
                player.weapon = weaponList[weapon_no]
            else:
            	print("You do not have enough gold.")
        # List items in shop
        if (action == 2):
            count = 1
            for item in itemList:
                print(str(count) + ") " + item.name +
                      " - Cost: " + str(item.gold))
                count += 1
            print("0) Back")
            # Get input for item choice
            item_no = int(input()) - 1

            # If player has enough gold, buy
            if (player.gold >= itemList[item_no].gold):
                player.gold -= itemList[item_no].gold
                itemList[item_no].use()

    # Show inventory
    elif (action == 3):
        os.system("clear")
        print(player.weapon.name + " - Dmg: " + str(player.weapon.minDmg) + "-" + str(player.weapon.maxDmg) +
              "\nGold: " + str(player.gold) + "\n")
    elif (action == 4):
    	os.system("clear")
    	print(player.name + "\nLvl: " + str(player.level) + "\nGold: " + str(player.gold) + "\nHealth: " + str(player.health) + "\nWeapon: " + (player.weapon.name) + "\n\nWins: " + str(player.wins) + "\nLosses: " + str(player.losses))
	# elif (action == 9):
	# 	os.system("clear")
	# 	print("")
    elif (action == 0):
        action = int(input('Are you sure you want to quit?\n1) Yes\n2) No\n'))
        if (action == 1):
            playing = False
        else:
            playing = True
