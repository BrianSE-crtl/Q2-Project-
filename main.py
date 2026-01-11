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

elif choice == '2':
    os.system('clear')
    singleTyping("About Me", delay=0.1)
    singleTyping("\nThis game was created by Brian Le.", delay=0.05)
    singleTyping("\n", delay=0.05)


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



