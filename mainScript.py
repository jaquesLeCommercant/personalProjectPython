# 1. clock system and events that add time // done
# 2. events arent prompted by the script, but by the player. idk if that makes sense. // done. very easy actually.
# 3. add needs (hunger, sleep, etc...) // not done
# 4. make needs fullfillment decerease as time goes. add ways to fullfill those needs (by eeping, eating, etc...) // not done
# 5. make a basic storyline with like events to go to school and study and do stuff like the rough shape. // not done
# once that's done, we'll have a working MVP.

### please SIMPLIFY THE CLOCK // done :D

firstName = input("What is your character's first name ? ")
lastName = input("What is your character's last name ? ")
# maybe add pronouns or something if player talks to npcs

time = 420


def show_clock():
    hour = time // 60
    minute = time % 60
    print(f"{hour:02d}:{minute:02d}")

def sleep():
    # set an alarm for an hour. how many time you sleep affects you. dont be like Hilda, sleep.
    print("console: sleep() called")

def breakfast():
    global time
    choiceBreakfast = input("you can choose to either [a] eat a snack bar (00:05) or [b] cook some beacon and eggs (00:20)")
    if choiceBreakfast == "a":
        print("you eat a snack bar. it aint really tasty, and it doesnt sustain you well.")
        time += 5
    elif choiceBreakfast == "b":
        print("You cook some beacon and eggs. Cooking takes time, but at least you eat a yummy and fullfilling breakfast.")
        time += 20
    else:
        print("annoying")

def study():
    # function to study. gonna be difficult, and i think its not needed yet for the MVP.
    print("console: study() called")

def checkPhone():
    # could always be useful.
    print("console: checkPhone() called")

def leaveBedroom():
    # youre gonna be late if you dont leave your home.
    print("console: leaveBedroom() called")

print(f"Yo {firstName}, you have to get up.")
show_clock()

# choice bedroom
choice_bedroom = input("""You stand in your bedroom. What do you do ?
[a] Sleep
[b] Eat breakfast
[c] Study
[d] Go on phone
[e] Go outside
""")

if choice_bedroom == "a":
    sleep()
elif choice_bedroom == "b":
    breakfast()
elif choice_bedroom == "c":
    study()
elif choice_bedroom == "d":
    checkPhone()
elif choice_bedroom == "e":
    leaveBedroom()
else:
    print("annoying")

show_clock()


# wait

choiceWait = input("you can choose to either (a) wait (00:57) or (b) wait (02:00) or (c) wait (07:43)")
if choiceWait == "a":
    print("you wait 57 minutes.")
    time += 57
elif choiceWait == "b":
    print("you wait 2 hours.")
    time += 120
elif choiceWait == "c":
    print("you wait 7 hours and 43 minutes.")
    time += 463
else:
    print("annoying")
    

show_clock()




## HUNGER
# hunger = 100
# and it decreases as time passes. once i get a gui, ill make it like a bar.

