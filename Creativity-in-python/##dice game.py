##dice game
import random
import math
points=0

while True:
    print("1)play more\n2)view points\n3)exit")
    D=int(input())
    if D==1:
        a=random.randrange(1,10)
        b=random.randrange(1,10)
        c=random.randrange(1,10)
        sum1=a+b+c
        print("the sum of 3 random numbers is ",sum1)
        print("Guess The Sum of the next 3 numbers")
        guess=int(input("enter the number"))
        a=random.randrange(1,10)
        b=random.randrange(1,10)
        c=random.randrange(1,10)
        sum2=a+b+c
        if guess-sum2==0:
            points=points+5
            print("good guess!! you havebeen awarded 5 points")
        elif guess>sum2:
            if (guess-sum2<=5) and (guess-sum2>=3):
                print("Not Bad Not Bad!!!you got 3 points")
                points=points+3
            elif (guess-sum2<3)and (guess-sum2>0):
                print("You almost got it  you got 4 points")
                points=points+4
            else:
                print("Sorry Better luck next time!! you got -",guess-sum2," points")
                points=points-(guess-sum2)
        elif sum2>guess:
            if (sum2-guess<=5) and (sum2-guess>=3):
                print("Not Bad Not Bad!!!you got 3 points")
                points=points+3
            elif (sum2-guess<3)and (sum2-guess>0):
                print("You almost got it you got 4 points")
                points=points+4
            else:
                print("Sorry Better luck next time!! you got -",sum2-guess," points")
                points=points-(sum2-guess)
        print("The sum was",sum2,"\nyou guessed",guess)
    elif D==2:
        print("you scored ",points)
    else:
        break




