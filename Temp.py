import pygetwindow as gw


blueStaks = gw.getWindowsWithTitle("BlueStacks App Player")[0]

blueStaks.moveTo(2200, 100)
blueStaks.resizeTo(1000, 800)
blueStaks.minimize()
blueStaks.restore()