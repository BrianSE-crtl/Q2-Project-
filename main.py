import os
import time

os.system('cls||clear')

# a simple typing effect
def singleTyping(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
        
        
# introduction / main menu
singleTyping("-------\n")
singleTyping("Hop Hop\n")
singleTyping("-------\n")
singleTyping("(\_/)\n")
singleTyping("( -_-)\n\n")
singleTyping("1. Play The Game\n")
singleTyping("2. About Me\n")
choice = input("Select an option (1 or 2)\n> ")


# first choice (main game)
if choice == '1':
    os.system('cls||clear')
    singleTyping("Waking up the rabbit...", delay=0.15)
    time.sleep(2)
    os.system('cls||clear')

    # rabbit display
    print("----------------")
    print("Clove The Rabbit")
    print("(\_/)")
    print("( •_•)")
    print("----------------")
    singleTyping("\nI am ready to hop!", delay=0.1)
    time.sleep(1.5)

    # game based stats and variables
    hops = 0
    
    multiplier = 1.0
    upgrade_level = 0
    upgrade_cost = 10
    
    last_time = time.time()

    # main game loop
    while True:
        current_time = time.time()
        if current_time - last_time >= 3.5:
            hops += 1 * multiplier
            last_time += 3.5

        os.system('cls||clear')
        print("----------------")
        print("Clove The Rabbit")
        print("(\_/)")
        print("( •_•)")
        print("----------------")
        print("Hops: " + str(int(hops)))
        print("Multiplier: x" + str(round(multiplier, 1)))
        
        # add an upgrade system if enough hops
        print("----------------")
        print("\nBug's Hop Shop")
        print("----------------")
        print("Hop Multiplier Upgrade")
        print("Level: " + str(upgrade_level))
        print("Cost: " + str(upgrade_cost) + " hops")
        print("\n(Upgrades are automatic so just watch hops increase!)")

        time.sleep(0.1) # tiny delay so the loop isn't crazy fast.