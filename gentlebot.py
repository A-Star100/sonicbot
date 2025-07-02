import os
import pyautogui
import random
import time
import threading

app_name = "Sonic GT"
# for macOS: os.system(f'osascript -e \'tell application "{app_name}" to activate\'')

print("Waiting 10 seconds... Get ready!")
time.sleep(10)

# Weighted keys for normal movement
keys = ['left'] * 2 + ['right'] * 2 + ['up'] * 5 + ['down'] * 2 + ['space'] * 3 + ['shift'] * 3

stop_bot = False

# Moveset combos
def spindash():
    print("Performing Spindash!")
    pyautogui.keyDown('shift')
    time.sleep(0.6)  # Hold longer
    pyautogui.keyUp('shift')  # Don't forget to release


def bounce():
    print("Performing Bounce!")
    pyautogui.keyDown('space')
    time.sleep(0.5)  # Hold jump
    pyautogui.keyUp('space')
    time.sleep(0.1)
    pyautogui.keyDown('shift')
    time.sleep(0.4)  # Hold dash
    pyautogui.keyUp('shift')

def homingAttack():
    print("Performing Homing Attack!")
    pyautogui.keyDown('space')
    time.sleep(0.5)  # Hold jump
    pyautogui.keyUp('space')
    time.sleep(0.1)

def dropDash():
    print("Performing Drop Dash!")
    pyautogui.keyDown('space')
    time.sleep(0.5)  # Hold jump
    pyautogui.keyUp('space')
    time.sleep(0.1)
    pyautogui.keyDown('ctrl')
    time.sleep(0.5)  # Hold jump
    pyautogui.keyUp('ctrl')
    time.sleep(0.1)


def lightSpeedDash():
    print("Performing Light Speed Dash!")
    pyautogui.keyUp('f')
    time.sleep(5)
    pyautogui.keyDown('f')

def goForward():
    print("Going very forward")
    pyautogui.keyUp('up')
    time.sleep(5)
    pyautogui.keyDown('up')

def goUpAndLeft():
    print("Going very left")
    pyautogui.keyUp('up')
    time.sleep(3)
    pyautogui.keyDown('up')
    pyautogui.keyUp('left')
    time.sleep(2)
    pyautogui.keyDown('left')

def goUpAndRight():
    print("Going very left")
    pyautogui.keyUp('up')
    time.sleep(3)
    pyautogui.keyDown('up')
    pyautogui.keyUp('right')
    time.sleep(2)
    pyautogui.keyDown('right')

def rollDownSlope():
    print("Rolling down slope")
    pyautogui.keyUp('up')
    time.sleep(0.2)
    pyautogui.keyUp('shift')
    time.sleep(4)
    pyautogui.keyDown('shift')
    pyautogui.keyDown('up')


def tricksss():
    print("TRICK TIME!")
    pyautogui.keyDown('space')
    time.sleep(0.4)
    pyautogui.keyUp('space')
    pyautogui.keyDown('z')
    # Randomly mash directional keys like tricks
    trick_keys = ['ctrl', 'shift', 'space', 'b']
    for _ in range(random.randint(2, 4)):
        key = random.choice(trick_keys)
        pyautogui.keyDown(key)
        time.sleep(1)
        pyautogui.keyUp(key)

    pyautogui.keyUp('z')




# Add more moves if needed
moveset = [spindash, bounce, homingAttack, lightSpeedDash, dropDash, goForward, goUpAndLeft, goUpAndRight, rollDownSlope, tricksss]

def wait_for_enter():
    global stop_bot
    input("Press ENTER to stop the bot...\n")
    stop_bot = True

threading.Thread(target=wait_for_enter, daemon=True).start()

print("Bot is now sending biased random key inputs with hold durations...")

try:
    while not stop_bot:
        # Occasionally perform a special move
        if random.random() < 0.2:  # 10% chance
            random.choice(moveset)()
        else:
            key = random.choice(keys)
            hold_time = random.uniform(0.3, 2.6)

            pyautogui.keyDown(key)
            print(f"Holding key: {key} for {hold_time:.2f} seconds")
            time.sleep(hold_time)
            pyautogui.keyUp(key)

        time.sleep(random.uniform(0.1, 0.3))

except KeyboardInterrupt:
    print("\nBot stopped manually.")

print("Bot stopped.")
