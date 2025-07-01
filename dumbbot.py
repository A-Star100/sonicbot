import os
import pyautogui
import time
import random
import threading

stop_bot = False

app_name = "Sonic GT"
os.system(f'osascript -e \'tell application "{app_name}" to activate\'')

def wait_for_enter():
    global stop_bot
    input("Press ENTER to stop DumbBot...\n")
    stop_bot = True

threading.Thread(target=wait_for_enter, daemon=True).start()

print("Me go fowardd")

try:
    while not stop_bot:
        # Always hold 'w' (forward)
        pyautogui.keyDown('up')
        print("Charging forward...")

        # Occasionally jump (like over nothing at all)
        if random.random() < 0.2:  # 20% chance per loop
            pyautogui.press('space')
            print("hElP mE")

        time.sleep(random.uniform(0.5, 1.2))

    pyautogui.keyUp('up')

except KeyboardInterrupt:
    pyautogui.keyUp('up')
    print("\nDumbBot stopped manually.")

print("DumbBot has stopped.")
