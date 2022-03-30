import time
import pyautogui


while True:
    pyautogui.press("scrolllock")
    time.sleep(30)
    print("pressed", flush=True)