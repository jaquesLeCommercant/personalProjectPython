# 1. clock system and events that add time // done
# 2. events arent prompted by the script, but by the player. idk if that makes sense. // not done and probably difficult
# 3. add needs (hunger, sleep, etc...) // not done
# 4. make needs fullfillment decerease as time goes. add ways to fullfill those needs (by eeping, eating, etc...) // not done
# 5. make a basic storyline with like events to go to school and study and do stuff like the rough shape. // not done
# once that's done, we'll have a working MVP.

### please SIMPLIFY THE CLOCK // done :D

name = input("What is your character's first name ? ")
# maybe add pronouns or something if player talks to npcs

time = 420


def show_clock():
    hour = time // 60
    minute = time % 60
    print(f"{hour:02d}:{minute:02d}")

print(f"Yo {name}, you have to get up.")
show_clock()

# breakfast

choiceBreakfast = input("you can choose to either eat a (a) snack bar (00:05) or (b) cook some beacon and eggs (00:20)")
if choiceBreakfast == "a":
    print("you eat a snack bar. it aint really yummy, and it doesnt sustain you well.")
    time += 5
elif choiceBreakfast == "b":
    print("you cook some tasty beacon and eggs. it takes a long time, but once your done you enjoy a delightful breakfast that sustains you well and makes you happier about your everyday life and makes you hopeful about the future.")
    time += 20
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
hunger = 100
# and it decreases as time passes. once i get a gui, ill make it like a bar.

