import pyautogui as p
import pywhatkit
def birthday_blast(pn, no_of_times, ):
    pywhatkit.sendwhatmsg(pn,"happy birthday",23,59,60)

    i=0
    while i<=no_of_times:
        p.write("happy birthdayz")
        p.press("enter")
        i=i+1
j=input("enter the phonenumber(including +91 and without spaces): ")
n=int(input("enter the number of times: "))
birthday_blast(j,n)
