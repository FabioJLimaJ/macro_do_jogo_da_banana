import pyautogui as py
import keyboard

py.keyDown('alt')
py.press(['tab'])
py.keyUp('alt')
py.sleep(5)

while True:
 py.click(clicks=100)
 if keyboard.is_pressed('Esc'):
        break