# sonicbot
A bot coded in Python that sends random keyboard inputs to your device, meant to play Sonic games (the stock code works with Sonic GT, if some controls are adjusted).
With some adjustments, it can work with any game, even Fortnite and Minecraft. It's all up to you.

Install dependencies via:
```shell
pip install -r requirements.txt
```

## speedybot.py (Recommended for Sonic games)
This bot is fast compared to the others and is skilled at basic movements such as the spindash, and extra combos.

## gentlebot.py
This bot is slower and his movements are more calculated compared to speedybot, but he has the same moveset.

## dumbbot.py
His sole purpose is for memes. He can only go forward and (occasionally) jump. Good luck with him.


## FAQ

1. Is this bot cross-platform?
   
   PyAutoGUI, the library used for sending keyboard inputs, is cross platform, so yes, the bots will work on any platform that supports keyboard usage.

2. What are the `['key'] * X` things?
   
   That is the key weighing system. Using it, certain keys will be pressed more than others via `random.choice()` in Python. Adjusting these values adjust the bias level per key. Not specifying     one means no bias for that key.

3. The bot doesn't work.
   
   In order for this bot to work (especially on macOS), you **must** allow Terminal (or the app running the script) to control your computer. Why? Otherwise, the bot cannot send inputs. It's        completely safe. If you're worried, check the code.
