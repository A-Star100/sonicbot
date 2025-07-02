import sys
import random
import time
import pyautogui
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QTextEdit, QLabel, QFileDialog
)
from PyQt5.QtCore import QThread, pyqtSignal


# --- Worker Thread that runs the bot ---
class BotThread(QThread):
    update_status = pyqtSignal(str)
    stop_signal = False

    def __init__(self, app_name):
        super().__init__()
        self.app_name = app_name

    def run(self):
        # For macOS: os.system(f'osascript -e \'tell application "{self.app_name}" to activate\'')
        self.update_status.emit("Waiting 5 seconds... Get ready!")
        time.sleep(5)

        keys = ['left'] * 2 + ['right'] * 2 + ['up'] * 5 + ['down'] * 2 + ['space'] * 3 + ['shift'] * 3
        moveset = [self.spindash, self.bounce, self.homingAttack, self.lightSpeedDash, self.dropDash, self.tricksss, self.uturn]

        self.update_status.emit("Bot started!")

        while not self.stop_signal:
            if random.random() < 0.2:
                move = random.choice(moveset)
                move()
            else:
                key = random.choice(keys)
                hold_time = random.uniform(0.2, 1.0)
                self.update_status.emit(f"Holding key: {key} for {hold_time:.2f}s")
                pyautogui.keyDown(key)
                time.sleep(hold_time)
                pyautogui.keyUp(key)

            time.sleep(random.uniform(0.05, 0.15))

        self.update_status.emit("Bot stopped.")
        self.stop_signal = False

    def stop(self):
        self.stop_signal = True

    # --- Move Functions ---
    def spindash(self):
        self.update_status.emit("Spindash!")
        pyautogui.keyDown('shift')
        time.sleep(0.4)
        pyautogui.keyUp('shift')

    def bounce(self):
        self.update_status.emit("Bounce!")
        pyautogui.keyDown('space')
        time.sleep(0.3)
        pyautogui.keyUp('space')
        time.sleep(0.1)
        pyautogui.keyDown('shift')
        time.sleep(0.3)
        pyautogui.keyUp('shift')

    def homingAttack(self):
        self.update_status.emit("Homing Attack!")
        pyautogui.keyDown('space')
        time.sleep(0.4)
        pyautogui.keyUp('space')

    def dropDash(self):
        self.update_status.emit("Drop Dash!")
        pyautogui.keyDown('space')
        time.sleep(0.4)
        pyautogui.keyUp('space')
        time.sleep(0.05)
        pyautogui.keyDown('ctrl')
        time.sleep(0.3)
        pyautogui.keyUp('ctrl')

    def lightSpeedDash(self):
        self.update_status.emit("Light Speed Dash!")
        pyautogui.keyDown('f')
        time.sleep(0.2)
        pyautogui.keyUp('f')

    def tricksss(self):
        self.update_status.emit("TRICK TIME!")
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

    def goForward(self):
        self.update_status.emit("Going very forward")
        pyautogui.keyUp('up')
        time.sleep(3)
        pyautogui.keyDown('up')

    def goUpAndLeft(self):
        self.update_status.emit("Going very left")
        pyautogui.keyUp('up')
        time.sleep(2)
        pyautogui.keyDown('up')
        pyautogui.keyUp('left')
        time.sleep(0.6)
        pyautogui.keyDown('left')

    def goUpAndRight(self):
        self.update_status.emit("Going very right")
        pyautogui.keyUp('up')
        time.sleep(2)
        pyautogui.keyDown('up')
        pyautogui.keyUp('right')
        time.sleep(0.6)
        pyautogui.keyDown('right')

    def rollDownSlope(self):
        self.update_status.emit("Rolling down slope")
        pyautogui.keyUp('up')
        time.sleep(0.1)
        pyautogui.keyUp('shift')
        time.sleep(3.5)
        pyautogui.keyDown('shift')
        pyautogui.keyDown('up')

    
    def uTurn(self):
        self.update_status.emit("Taking a u-turn")
    
        # Release forward key
        pyautogui.keyUp('up')
    
        # Simulate slight turn prep
        pyautogui.keyDown('left')
        time.sleep(0.3)
        pyautogui.keyUp('left')

        # Turn around and go full speed in opposite direction
        pyautogui.keyDown('down')
        time.sleep(1.0)
        pyautogui.keyUp('down')
    


# --- GUI Window ---
class BotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SonicBot")
        self.setFixedSize(450, 320)

        self.app_name = None
        self.bot_thread = None

        self.layout = QVBoxLayout()

        self.label = QLabel("SonicBot")
        self.app_label = QLabel("No app selected.")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.select_button = QPushButton("Select Game App (.app)")
        self.start_button = QPushButton("Start Bot")
        self.stop_button = QPushButton("Stop Bot")

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.app_label)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        self.setLayout(self.layout)

        # Connect signals
        self.select_button.clicked.connect(self.select_app)
        self.start_button.clicked.connect(self.start_bot)
        self.stop_button.clicked.connect(self.stop_bot)

    def log(self, message):
        self.output.append(message)

    def select_app(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select .app file",
            "/Applications",
            "Applications (*.app)"
        )

        if path and path.endswith(".app"):
            self.app_name = os.path.basename(path).replace(".app", "")
            self.app_label.setText(f"Selected App: {self.app_name}")
            self.log(f"App selected: {self.app_name}")
            self.start_button.setEnabled(True)
        else:
            self.log("Invalid selection. Please choose a valid .app file.")

    def start_bot(self):
        self.output.clear()
        self.bot_thread = BotThread(self.app_name)
        self.bot_thread.update_status.connect(self.log)
        self.bot_thread.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_bot(self):
        if self.bot_thread:
            self.bot_thread.stop()
            self.bot_thread.wait()
            self.bot_thread = None
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

# --- Main ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BotGUI()
    window.show()
    sys.exit(app.exec_())
