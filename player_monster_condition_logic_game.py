# Build Text based RPG game

""" Write a text-based role-playing game(RPG) with the following features:
1). The game involves one player and one monster. 
2). The player begins with 100 health, while the monster starts with 150 health.
3). The player has the option to attack, heal, or run away
4). If the player attacks, they deal between 10 and 15 damage to the monster. 
5). If the player heals, they regain 30 health, but that can’t go over their maximum of 100.
6). If the player runs away, then the game ends.
7). After the player’s turn, if the monster is still alive—then it deals between 15 and 20 damage to the player."""


######################STRETCH#############################

# Prevent the player from exiting the game.
#    By pressing Ctrl + C.
# Introduce double-damage critical hits.
# That accour when an attack value is a mutiple of 3.
# Use emojis or string formatting syntax 
# TO make the game output more enjoyable  


import random 

print("Welcome to the role-playing game!")

#1). The game involves one player and one monster. 
#2). The player begins with 100 health, while the monster starts with 150 health.

player_health = 100
monster_health = 150
heal = 30

def is_factor_three(number):
    if number % 3 == 0:
        return True
    else:
        return False

def calculate_damage_number(attacker):
    if attacker == "player":
        damage = random.randint(10,15)
    else:
        damage = random.randint(15,20)

    if is_factor_three(damage):
        damage = damage * 2
        print(f"👾{attacker.capitalize()} scored a critical hit of {damage} damage.")
    
    return damage


while True:
    #3). The player has the option to attack, heal, or run away
    
    print(f" ❤️ Your Health : {player_health}, Monster Health: {monster_health}")
    try:
        action = input("Do you want to (A)ttack, (H)eal or (R)un away: ").upper()
    except KeyboardInterrupt:
        print("\n ❌ You can't game quit using ctrl + c")
        continue  # Continue the loop if Ctrl+C is pressed
         
    #4). If the player attacks, they deal between 10 and 15 damage to the monster. 

    if action == "A":
        damage = calculate_damage_number("player")
        monster_health -= damage
        print(f" 🥷 You attacked the monster for {damage} damage!")

        if monster_health <= 0:
            print(" 🏆 You defeated the monster!")
            break

    #5). If the player heals, they regain 30 health, but that can’t go over their maximum of 100.

    elif action == "H":
        player_health += heal
        if player_health > 100:
            player_health = 100
        print(f" ❤️ You healed for {heal} health!")

    #6). If the player runs away, then the game ends.    
        
    elif action == "R":
        print(" 🏃‍♂️ You'r run away.")
        break 
    else:
        print(" ❌ Invalid Action! Please Choose Valid Action Option 'A','H', or 'R'")
        continue
    #7). After the player’s turn, if the monster is still alive—then it deals between 15 and 20 damage to the player."""
    if monster_health > 0:
        monster_damage = calculate_damage_number("monster")
        player_health -= monster_damage
        print(f" 👹 The monster attacked you for {monster_damage} damage!")

        if player_health <= 0:
            print(" 😈 You were defeated by the monster!")
            break

print("Game Over!")


