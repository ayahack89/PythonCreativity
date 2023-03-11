import pyautogui as p
import time as t
import webbrowser as w
#online class joiner
while True:
    hour=t.strftime("%H")
    min=t.strftime("%M")
    # print(hour,min) for testing pourpose
    if (hour==12 and min==00) or(hour==13 and min==00)or (hour==16 and min==00 ):
        w.open("https://classroom.google.com/u/1/c/NTM4NjkxNjQ0NzUw")
        t.sleep(20)
        p.moveTo(x=486, y=613)
        p.leftClick()
        t.sleep(25)
        p.keyDown("ctrl")
        p.press("e")
        p.press("d")
        p.keyUp("ctrl")

        p.moveTo(x=1381, y=565)
        p.leftClick()

    t.sleep(60)
