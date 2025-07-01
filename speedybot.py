import os
import pyautogui
import random
import time
import threading

app_name = "Sonic GT"
# For macOS: os.system(f'osascript -e \'tell application "{app_name}" to activate\'')

print("Waiting 5 seconds... Get ready!")
time.sleep(5)

# Weighted keys for normal movement
keys = ['left'] * 2 + ['right'] * 2 + ['up'] * 5 + ['down'] * 2 + ['space'] * 3 + ['shift'] * 3

stop_bot = False

# Moveset combos
def spindash():
    print("Performing Spindash!")
    pyautogui.keyDown('shift')
    time.sleep(0.4)
    pyautogui.keyUp('shift')

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

def lightSpeedDash():
    print("Performing Light Speed Dash!")
    pyautogui.keyDown('f')
    time.sleep(0.2)
    pyautogui.keyUp('f')

def goForward():
    print("Going very forward")
    pyautogui.keyUp('up')
    time.sleep(3)
    pyautogui.keyDown('up')

def goUpAndLeft():
    print("Going very left")
    pyautogui.keyUp('up')
    time.sleep(2)
    pyautogui.keyDown('up')
    pyautogui.keyUp('left')
    time.sleep(0.6)
    pyautogui.keyDown('left')

def goUpAndRight():
    print("Going very right")
    pyautogui.keyUp('up')
    time.sleep(2)
    pyautogui.keyDown('up')
    pyautogui.keyUp('right')
    time.sleep(0.6)
    pyautogui.keyDown('right')

def rollDownSlope():
    print("Rolling down slope")
    pyautogui.keyUp('up')
    time.sleep(0.1)
    pyautogui.keyUp('shift')
    time.sleep(3.5)
    pyautogui.keyDown('shift')
    pyautogui.keyDown('up')


def tricksss():
    print("TRICK TIME!")
    pyautogui.keyDown('space')
    time.sleep(0.4)
    pyautogui.keyUp('space')
    pyautogui.keyDown('t')
    # Randomly mash directional keys like tricks
    trick_keys = ['left', 'right', 'up', 'down']
    for _ in range(random.randint(2, 4)):
        key = random.choice(trick_keys)
        pyautogui.press(key)
        time.sleep(0.1)

    pyautogui.keyUp('t')


# Add more moves if needed
moveset = [spindash, bounce, homingAttack, lightSpeedDash, dropDash, goForward, goUpAndLeft, goUpAndRight, rollDownSlope, tricksss]

def wait_for_enter():
    global stop_bot
    input("Press ENTER to stop the bot...\n")
    stop_bot = True

threading.Thread(target=wait_for_enter, daemon=True).start()

print("Bot is now sending biased random key inputs with shorter delays...")

try:
    while not stop_bot:
        # Occasionally perform a special move
        if random.random() < 0.2:
            random.choice(moveset)()
        else:
            key = random.choice(keys)
            hold_time = random.uniform(0.2, 1.0)

            pyautogui.keyDown(key)
            print(f"Holding key: {key} for {hold_time:.2f} seconds")
            time.sleep(hold_time)
            pyautogui.keyUp(key)

        # Faster cycle
        time.sleep(random.uniform(0.05, 0.15))

except KeyboardInterrupt:
    print("\nBot stopped manually.")

print("Bot stopped.")
