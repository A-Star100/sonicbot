import pyautogui
import random
import time
import threading

stop_bot = False

# Basic movement keys for 2D Sonic
keys = ['right'] * 5 + ['z'] * 3 + ['down'] + ['shift']

def spindash():
    print("Performing Spindash (down + shift)")
    pyautogui.keyDown('down')
    time.sleep(0.2)
    pyautogui.keyDown('shift')
    time.sleep(0.3)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('down')

def jump():
    print("Jumping!")
    pyautogui.keyDown('space')
    time.sleep(0.2)
    pyautogui.keyUp('space')

def roll():
    print("Rolling (shift)")
    pyautogui.keyDown('shift')
    time.sleep(0.3)
    pyautogui.keyUp('shift')

moveset = [spindash, jump, roll]

def wait_for_enter():
    global stop_bot
    input("Press ENTER to stop the 2D bot...\n")
    stop_bot = True

threading.Thread(target=wait_for_enter, daemon=True).start()

print("Starting 2D Sonic bot in 5 seconds...")
time.sleep(5)
print("Bot is now running. Playing randomly...")

try:
    while not stop_bot:
        if random.random() < 0.25:
            random.choice(moveset)()
        else:
            key = random.choice(keys)
            duration = random.uniform(0.2, 0.5)
            pyautogui.keyDown(key)
            print(f"Holding key: {key} for {duration:.2f}s")
            time.sleep(duration)
            pyautogui.keyUp(key)

        time.sleep(random.uniform(0.05, 0.2))

except KeyboardInterrupt:
    print("Stopped manually.")

print("Bot stopped.")
