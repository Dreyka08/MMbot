import pyautogui
import cv2 
import numpy as np
import subprocess
import time

Gift = cv2.imread("imgs/GIFT.png")
Start = cv2.imread("imgs/Start.png")
prod = cv2.imread("imgs/Prod.png")
Home = cv2.imread("imgs/OK.png")
Camp = cv2.imread("imgs/Campani.png")
AutoBattle = cv2.imread("imgs/AutoBattle.png")
GoToBattle = cv2.imread("imgs/InBattle.png")
NewTurn = cv2.imread("imgs/NewTurn.png")
continuePlay =  cv2.imread("imgs/Continue.png")

def searchOnScreen(target, screen):
    result = cv2.matchTemplate(target, screen, cv2.TM_CCOEFF_NORMED)
    locations = []
    for y, x in zip(*np.where(result >= 0.85)):
        locations.append((x, y))
    if len(locations) != 0:
        answer = [locations[0][0] + 10, locations[0][1] + 10]
        return answer
    else:       
        return []

def takeScreen():
    screen = pyautogui.screenshot()
    screen.save("imgs/temp.png")
    screen = cv2.imread("imgs/temp.png")
    return screen

def BattleStart():
    ans = []
    while len(ans) == 0:
        target = GoToBattle
        screen = takeScreen()
        ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    ans = []
    while len(ans) == 0:
        target = AutoBattle
        screen = takeScreen()
        ans = searchOnScreen(target, screen) 

    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    ans = []
    while len(ans) == 0:
        target = continuePlay
        screen = takeScreen()
        ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()

def MainGame():
    screen = takeScreen()
    target = Start
    ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    ans = []
    while len(ans) == 0:
        target = Home
        screen = takeScreen()
        ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    time.sleep(2)
    screen = takeScreen()
    target = Camp
    ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    time.sleep(2)
    screen = takeScreen()
    target = prod
    ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1000, 305)
    pyautogui.click()
    ans = []
    while len(ans) == 0:
        target = Gift
        screen = takeScreen()
        ans = searchOnScreen(target, screen)
    pyautogui.moveTo(ans[0], ans[1])
    pyautogui.click()
    
    while 1:
        screen = takeScreen()

        target = NewTurn
        target2 = GoToBattle
    
        ans = searchOnScreen(target, screen)
        ans2 = searchOnScreen(target2, screen)
        if len(ans2) != 0:
            BattleStart()
            
        else:
            pyautogui.moveTo(ans[0], ans[1])
            pyautogui.click()
    
MainGame()