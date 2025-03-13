import time
from pypresence import Presence

client_id = input("Enter your application's client ID: ")
details = input("Enter the details (First Line): ")
state = input("Enter the state (Second Line): ")
large_image = input("Enter the key for the large image: ")
small_image = input("Enter the key for the small image: ")

print("Your Rich Presence is now running! Look in the Discord client to see it.")

RPC = Presence(client_id)
RPC.connect()

def update_presence():
    RPC.update(state=state, details=details, large_image=large_image, small_image=small_image)

update_presence()

try:
    while True:
        time.sleep(15)  # Can only update presence every 15 seconds
        change = input("Do you want to change the details, state, or images? (yes/no): ").strip().lower()
        if change == 'yes':
            details = input("Enter the new details (First Line): ")
            state = input("Enter the new state (Second Line): ")
            large_image = input("Enter the new key for the large image: ")
            small_image = input("Enter the new key for the small image: ")
            update_presence()
except KeyboardInterrupt:
    RPC.close()