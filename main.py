import webbrowser
import pyautogui
import time
from PIL import ImageGrab

URL = "https://elgoog.im/t-rex/"

# CONSTANTS
GAME_RUNNING = True
Y_JUMP = 800
X_JUMP = [num for num in range(750, 800)]
X_JUMP_2 = [num for num in range(750, 900)]
X_JUMP_3 = [num for num in range(750, 1000)]
X_JUMP_4 = [num for num in range(750, 1150)]
PERFORMED_JUMPS = 0
GAME_OVER_X = [num for num in range(979, 988)]
GAME_OVER_Y = [num for num in range(495, 524)]


# Opens tab and starts game by performing one jump
def start_game():
    webbrowser.open_new_tab(URL)
    time.sleep(6)
    pyautogui.press('up')
    time.sleep(2)
    pyautogui.keyDown("down")


# dino performs a jump and when necessary distance from where dino starts jump movement is increased to adapt to game speed
def jump():
    pyautogui.keyUp("down")
    pyautogui.press('up')
    global PERFORMED_JUMPS
    global X_JUMP
    PERFORMED_JUMPS += 1
    if PERFORMED_JUMPS == 9:
        X_JUMP = X_JUMP_2
    if PERFORMED_JUMPS == 15:
        X_JUMP = X_JUMP_3
    if PERFORMED_JUMPS == 22:
        X_JUMP = X_JUMP_4
    time.sleep(0.3)
    pyautogui.keyDown("down")


def check_game_over(img):
    for x_coord in GAME_OVER_X:
        for y_coord in GAME_OVER_Y:
            if img.getpixel(tuple([x_coord, y_coord])) != (83, 83, 83):
                return
            global GAME_RUNNING
            GAME_RUNNING = False


def play_game():
    start_game()
    while GAME_RUNNING:
        time.sleep(0.005)
        img = ImageGrab.grab()
        for x_coord in X_JUMP:
            if img.getpixel(tuple([x_coord, Y_JUMP])) != (255, 255, 255):
                jump()
                break

        check_game_over(img)


if __name__ == '__main__':
    play_game()