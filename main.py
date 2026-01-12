import os 
import time 
from turtle import delay
os.system('clear')

def singleTyping(text, delay=0.2):
    for char in text:
        print(char, end="", flush=True)  # print each letter without newline (flush ensures it appears immediately)
        time.sleep(delay)   # wait a bit between letters
        
        
# menu options 
print("Menu Options:")
print("1. Play The Game")
print("2. About Me")
print("3. Reset Progress (WIPES ALL DATA/PROGRESSION)")

choice = input("Select an option (1, 2, or 3): ")

# playing the game section
if choice == '1':
    os.system('clear')
    singleTyping("Waking up the rabbit...", delay=0.15)
    time.sleep(2)
    os.system('clear')

    # rabbit intro 
    singleTyping("-----------------------", delay=0.02)
    singleTyping("\nClove The Rabbit", delay=0.1)
    singleTyping("\n(\_/)", delay=0.09)
    singleTyping("\n( •_•)", delay=0.09)
    singleTyping("\n-----------------------", delay=0.02)
    singleTyping("\nI am ready to hop!", delay=0.1)

# about me section
elif choice == '2':
    os.system('clear')
    singleTyping("About Me", delay=0.1)
    singleTyping("\n---------", delay=0.05)
    singleTyping("\nHello! My name is Brian Le, and I am the creator of this game.", delay=0.05)
    singleTyping("\nI am a passionate intermediate developer who loves creating fun and engaging experiences.", delay=0.05)
    singleTyping("\nThank you for playing one of my projects!", delay=0.05)
    singleTyping("\n~1/11/26", delay=0.05)
    
# reset progress section
elif choice == '3':
    os.system('clear')
    choice_confirm = input("Are you sure you want to reset all progress? This action cannot be undone. (yes/no): ")
    if choice_confirm.lower() == 'yes':
        singleTyping("Resetting all progress...", delay=0.1)
        time.sleep(1)
        os.system('clear')
        hops = 0 # reset hops count to 0
        singleTyping("All progress has been reset.", delay=0.1)
    




# # hops count
# hops = 0

# # hops functionality
# last_time = time.time()

# while True:
#     current_time = time.time()

#     if current_time - last_time >= 5:
#         hops += 1
#         last_time = current_time
#         print(f"\rHops: {hops}", end="")



