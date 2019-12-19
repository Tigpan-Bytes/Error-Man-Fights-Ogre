flag = "FLAG_IS_HERE_IN_EXE_VERSION"

from time import sleep

def ensure_acceptable_choice(choice):
    if choice == 'a' or choice == 's':
        return choice
    return ensure_acceptable_choice(input("Invalid choice, please only (a)ttack or (s)pell.\n"))

def ensure_acceptable_spell(spell, mana):
    if spell == 'v' or spell == 'f' or spell == 'r' or spell == 'c':
        if (spell == 'v' and mana < 10) or (spell == 'f' and mana < 5) or (spell == 'r' and mana < 5):
            return ensure_acceptable_spell(input("Not enough mana [you have " + str(mana) + " mana], (v)eil [10 mana], (f)lex [5 mana], (r)age [5 mana], or (c)ancel and attack.\n"), mana)
        return spell
    return ensure_acceptable_spell(input("Invalid choice, please only (v)eil [10 mana], (f)lex [5 mana], (r)age [5 mana], or (c)ancel and attack.\n"), mana)


print("\nThis is an in-progress open-source game, please contribute at [https://github.com/Tigpan-Bytes/Error-Man-Fights-Ogre]!\n")
print("This game is called 'ERROR MAN FIGHTS OGRE', you play as ErrorMan and you fight an Ogre.")
print("Soon this will be sold on steam for $89.99 ($119.99 for the collectors edition). I just need to submit it.")
sleep(3)
print("\nYou are walking down a path...")
sleep(2)
print("\nYou are still walking...")
sleep(2)

while True:
    print("\nYou encounter an Ogre! What a surprise!!!\n")
    sleep(1.5)

    player_health = 40
    player_mana = 40
    ogre_health = 60

    is_player_turn = True

    veil_count = 0 # holds the amount of turns to be veiled for
    has_flex = False # holds if the critical spell is active

    try:
        while player_health > 0 and ogre_health > 0:
            if is_player_turn:
                print("Error Man:\n  -> Health: " + str(player_health) + " / 40 \n  -> Mana: " + str(player_mana) + " / 40")
                print("Ogre:\n  -> Health: " + str(ogre_health) + " / 60")

                choice = ensure_acceptable_choice(input("Select (a)ttack or (s)pell.\n"))
                spell = ""
                if choice == 's':
                    spell = ensure_acceptable_spell(input("Select (v)eil [10 mana], (f)lex [5 mana], (r)age [5 mana], or (c)ancel and attack.\n"), player_mana)
                    if spell == 'v':
                        veil_count = 2
                        print("You put up a veil of shadows and are protected against 2 attacks!")
                        player_mana -= 10

                    if spell == 'f':
                        has_flex = True
                        print("You flex your massive muscles, powering up your next attack.")
                        player_mana -= 5

                    if spell == 'r':
                        damage = 20 * (3 if has_flex else 1)
                        print("You attack with an intense rage, dealing " + str(damage) + " damage!")
                        print("However you hit yourself for 1 damage in your rage!")
                        ogre_health -= damage
                        player_health -= 1
                        player_mana -= 5

                if choice == 'a' or spell == 'c':
                    damage = 10 * (3 if has_flex else 1)
                    print("You attack the ogre for " + str(damage) + " damage!")
                    ogre_health -= damage

                sleep(0.5)
            else:
                if veil_count > 0:
                    print("The ogre attempts to attack you, but you are veiled!")
                    sleep(0.25)
                    veil_count -= 1
                    if veil_count == 1:
                        print("You have 1 more turn of protection.")
                    else:
                        print("Your veil is depleted")
                    sleep(0.5)
                else:
                    print("The ogre attacks you for 8 damage!")
                    player_health -= 8
                    sleep(0.5)
            is_player_turn = not is_player_turn
            print("")

        if player_health <= 0:
            print("Oh no, you lost. Better luck next time.")
        if ogre_health <= 0:
            print("Well done you beat the ogre!\n")
            damage_taken = 40 - player_health
            damage_dealt = 60 - ogre_health
            print("You took " + str(damage_taken) + " damage, but dealt " + str(damage_dealt) + " damage to the ogre.")

            ratio = damage_dealt / damage_taken
            print("That means you dealt " + str(round(ratio * 100)) + "% of the damage you took!")
    except:
        # If you can cause the game to error, then you get the flag
        print("ERROR ERROR ERROR!!!")
        print("Flag = " + flag)

    input("\nPress enter to play again.\n")
