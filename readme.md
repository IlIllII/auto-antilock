# Auto Antilock

Have you ever wanted to go grab a coffee but didn't want your screen to lock for whatever reason, but you also didn't want to change your settings just to change them back again when you got back? Then this script is for you!

This script keeps your screen from locking by toggling the scroll lock every so often.

## Instructions

Navigate your terminal to the directory containing this script and type:

```bash
py antilock.py
```

The script will then run indefinitely until you stop it by either interrupting the program or closing your terminal. You can tell that it is running by the blinking cursor on your keyboard or just by the fact that the screen is not locked.

By default the button toggles every 10 minutes, but you may need to toggle it faster depending on your screen lock settings. In that case, just pass the number of minutes you want your desired toggle frequency to be as an argument to the script like so:

```bash
py antilock.py 5
```

The above command will toggle the scroll lock every 5 minutes.

Finally, the script uses pyautogui to toggle the button. If you don't have this module installed, you can install it by typing:

```bash
pip install pyautogui
```