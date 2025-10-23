import pyautogui
import cv2 
import mss
import mss.tools
import numpy as np
import pygetwindow as gw

# Account
BBack = cv2.imread("imgs/Back.png")
BAccount = cv2.imread("imgs/Account.png")
BEntrAcc = cv2.imread("imgs/EntrAcc.png")
Bvk = cv2.imread("imgs/VK.png")
Bvkcon = cv2.imread("imgs/VKcon.png")

# Base
BHome = cv2.imread("imgs/OK.png")
BHome2 = cv2.imread("imgs/OK2.png")
BCross = cv2.imread("imgs/Cross.png")
BCross2 = cv2.imread("imgs/Cross2.png")

# Campany
BCamp = cv2.imread("imgs/Campani.png")
BProd = cv2.imread("imgs/Prod.png")
BDayStart = cv2.imread("imgs/DayStart.png")

#Gift
BGift = cv2.imread("imgs/GIFT.png")
BDGift = cv2.imread("imgs/DayGift.png")

BStart = cv2.imread("imgs/Start.png")

# Battle
BGoToBattle = cv2.imread("imgs/InBattle.png")
BAutoBattle = cv2.imread("imgs/AutoBattle.png")
BContinuePlay =  cv2.imread("imgs/Continue.png")

BNewTurn = cv2.imread("imgs/NewTurn.png")


blueStaks = gw.getWindowsWithTitle("BlueStacks App Player")[0]
blueStaks.moveTo(2400, 100)
blueStaks.resizeTo(1400, 800)
blueStaks.minimize()
blueStaks.restore()

def takeScreen():
    with mss.mss() as sct:
        monitors = sct.monitors
        for i, monitor in enumerate(monitors[1:], 1):  # Пропускаем первый (общий)
            screenshot = sct.grab(monitor)
            filename = f"imgs/temp.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
        return cv2.imread("imgs/temp.png")

def searchOnScreen(target, screen):
    result = cv2.matchTemplate(target, screen, cv2.TM_CCOEFF_NORMED)
    locations = []
    for y, x in zip(*np.where(result >= 0.6)):
        locations.append((x, y))
    if len(locations) != 0:
        answer = [locations[0][0] + 10, locations[0][1] + 10]
        return answer
    else:       
        return []

def clickOnM(img, t):
    ans = []
    while len(ans) == 0:
        screen = takeScreen()
        ans = searchOnScreen(img, screen)
    x, y = pyautogui.position()
    pyautogui.moveTo(ans[0] + (2000 - t), ans[1] + 20)
    pyautogui.click()
    pyautogui.moveTo(x, y)

def clickOn(img):
    ans = []
    while len(ans) == 0:
        screen = takeScreen()
        ans = searchOnScreen(img, screen)
    x, y = pyautogui.position()
    pyautogui.moveTo(ans[0] + 2000, ans[1] + 20)
    pyautogui.click()
    pyautogui.moveTo(x, y)

def pickbetween(FWay, SWay):
    ansf = []
    anss = []
    screen = takeScreen()
    ansf = searchOnScreen(FWay, screen)
    anss = searchOnScreen(SWay, screen)
    if len(ansf) >= len(anss):
        return 1
    else:
        return 2

def RestoreAccount():
    clickOn(BBack)
    clickOn(BAccount)
    clickOn(BEntrAcc)
    clickOn(Bvk)
    clickOn(Bvkcon)
    clickOn(BHome)
    clickOnM(BCross, 100)

def EnterCompany():
    clickOn(BCamp)
    clickOn(BProd)
    clickOn(BDayStart)

def FirstEnterPerDay():
    clickOn(BHome2)
    clickOn(BHome2)
    EnterCompany()
    clickOnM(BGift, 30)
    clickOn(BDGift)
    clickOn(BHome)
    clickOnM(BCross2, 30)

def Battle():
    clickOn(BGoToBattle)
    clickOnM(BAutoBattle, 25)
    clickOn(BContinuePlay)

def Main():
    # RestoreAccount()
    # FirstEnterPerDay()
    while True:
        check = pickbetween(BGoToBattle, BNewTurn)
        if check == 1:
            Battle()
        else:
            clickOn(BNewTurn)

Main()