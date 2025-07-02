import os
import pyautogui
import random
import time
import threading
from datetime import datetime

app_name = "Sonic GT"
# for macOS: os.system(f'osascript -e \'tell application "{app_name}" to activate\'')

print("Waiting 5 seconds... Get ready!")
time.sleep(5)

# Movement keys with weighted randomness
movement_keys = ['left'] * 2 + ['right'] * 2 + ['up'] * 5 + ['down'] * 2

def smart_key_press(key):
    duration = 0.1 if key in ['left', 'right'] else random.uniform(0.3, 0.7)
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# Cooldown tracker
cooldowns = {}

def is_ready(move_name, cooldown=5):
    return time.time() - cooldowns.get(move_name, 0) > cooldown

def record_cooldown(move_name):
    cooldowns[move_name] = time.time()

# Moveset definitions
def spindash():
    if not is_ready('spindash'): return
    print("Performing Spindash!")
    pyautogui.keyDown('shift')
    time.sleep(0.4)
    pyautogui.keyUp('shift')
    record_cooldown('spindash')

def bounce():
    print("Performing Bounce!")
    pyautogui.keyDown('space')
    time.sleep(0.3)
    pyautogui.keyUp('space')
    time.sleep(0.1)
    pyautogui.keyDown('shift')
    time.sleep(0.3)
    pyautogui.keyUp('shift')

def homingAttack():
    print("Performing Homing Attack!")
    pyautogui.keyDown('space')
    time.sleep(0.4)
    pyautogui.keyUp('space')

def dropDash():
    print("Performing Drop Dash!")
    pyautogui.keyDown('space')
    time.sleep(0.4)
    pyautogui.keyUp('space')
    time.sleep(0.05)
    pyautogui.keyDown('ctrl')
    time.sleep(0.3)
    pyautogui.keyUp('ctrl')

def tricksss():
    print("TRICK TIME!")
    pyautogui.keyDown('space')
    time.sleep(0.4)
    pyautogui.keyUp('space')
    pyautogui.keyDown('z')
    trick_keys = ['ctrl', 'shift', 'space', 'b']
    for _ in range(random.randint(2, 4)):
        key = random.choice(trick_keys)
        pyautogui.keyDown(key)
        time.sleep(0.5)
        pyautogui.keyUp(key)
    pyautogui.keyUp('z')

# Modes
modes = ['explore', 'trick', 'speed']

# Behavior engine
stop_bot = False
last_action = None

def choose_move():
    r = random.random()
    if r < 0.2:
        return spindash
    elif r < 0.4:
        return homingAttack
    elif r < 0.6:
        return dropDash
    elif r < 0.8:
        return tricksss
    else:
        return random_movement

def random_movement():
    key = random.choice(movement_keys)
    smart_key_press(key)

# Stopper thread
def wait_for_enter():
    global stop_bot
    input("Press ENTER to stop the bot...\n")
    stop_bot = True

threading.Thread(target=wait_for_enter, daemon=True).start()

print("Smarter Sonic bot running...")
try:
    while not stop_bot:
        action = choose_move()
        action()
        time.sleep(random.uniform(0.1, 0.25))

except KeyboardInterrupt:
    print("\nBot stopped manually.")

print("Bot stopped.")
