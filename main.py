import time

import pyautogui

lista = ["Goland", "RubyMine", "PgAdmin", "Conduktor", "filezil", "slack", "pgAdmi"]


if __name__ == '__main__':
    for l in lista:
        time.sleep(2)
        pyautogui.keyDown('command')
        pyautogui.press(['space'])
        pyautogui.keyUp('command')
        pyautogui.write(l)
        pyautogui.press(['enter'])






