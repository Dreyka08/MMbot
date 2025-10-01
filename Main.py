import pyautogui
import cv2 #pip install opencv-python
import numpy as np

target = cv2.imread("inBattle.png")
screen = pyautogui.screenshot()
screen.save("imgs/temp.png")
screen = cv2.imread("imgs/temp.png")


pyautogui.moveTo(x, y)
pyautogui.click()

def search(target, scren):
    result = cv2.matchTemplate(target, scren, cv2.TM_CCOEFF_NORMED)
    locations = []
    for y, x in zip(*np.where(result >= 0.8)):
        locations.append((x, y))
    answer = [locations[0][0] + 5, locations[0][1] + 5]
    return answer
