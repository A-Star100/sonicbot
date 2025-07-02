# sonicbot
A bot coded in Python that sends random keyboard inputs to your device, meant to play Sonic games (the stock code works with Sonic GT, if some controls are adjusted, and Sonic BTS).
With some adjustments, it can work with any game, even Fortnite and Minecraft. It's all up to you.

Install dependencies via:
```shell
pip install -r requirements.txt
```

## smartbot.py (Recommended for Sonic games)
This formidable bot uses even more decision making, taking his chances and based on his decision, deciding which path to take next, all with smart cooldowns being the cherry on top. He's by far the best at navigating levels and pathways compared to the others, but every bot excels in one way or another.

## speedybot.py (Also recommended for Sonic games)
This bot is fast compared to the others (except smartbot) and is skilled at basic movements such as the spindash, and extra combos.
While not as precise as smartbot, he is better at veering himself the right direction (instead of being in the wrong one) to make up for his slight disadvantages.

## speedybot-gui.py
The same as the original **speedybot.py** but with a user-friendly GUI with PyQT 5.

## gentlebot.py
This bot is slower and his movements are more calculated compared to speedybot, but he has the same moveset.

## dumbbot.py
His sole purpose is for memes. He can only go forward and (occasionally) jump. Good luck with him.

## 2dbot.py
A completely different bot optimized for 2D games such as Sonic Before The Sequel and more.


## FAQ

1. Is this bot cross-platform?
   
   PyAutoGUI, the library used for sending keyboard inputs, is cross platform, so yes, the bots will work on any platform that supports keyboard usage & Python (Windows, macOS, Linux, and more).

2. What are the `['key'] * X` things?
   
   That is the key weighing system. Using it, certain keys will be pressed more than others via `random.choice()` in Python (because when you multiply an array, it is basically copied, so `['up'] * 4` means `['up'] + ['up'] + ['up'] + ['up']` in the code). Adjusting these values adjust the bias level per key. Not specifying     one means no bias for that key.

4. The bot doesn't work.
   
   In order for this bot to work (especially on macOS), you **must** either run as admin (Windows) or allow Terminal (or the app running the script) to control your computer (macOS). Why?           Otherwise, the bot cannot send inputs, or **[you haven't mapped the keys correctly](https://github.com/A-Star100/sonicbot/blob/main/KEYS.md)**. It's completely safe. If you're worried, check the code.
