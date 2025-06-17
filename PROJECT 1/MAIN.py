
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer= random.choice([1,0,-1])
youstr=input("ENTER YOUR CHOICE: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"SNAKE",-1:"WATER",0:"GUN"}
you=youdict[youstr]
a=reversedict[you]
b=reversedict[computer]
# By now we have 2 numbers (variables), you and computer
print("YOU CHOSE: ",a,"\nCOMPUTER CHOSE: ",b)

if (computer==you):
    print("IT'S A DRAW!!")
else:
    if (computer==1 or you==-1):
        print("RESULT: YOU LOOSE!")
    elif (computer==1 or you==0):
        print("RESULT: YOU WIN!")
    elif (computer == -1 or you == 1):
        print("RESULT: YOU WIN!")
    elif (computer == -1 or you == 0):
        print("RESULT: YOU LOOSE!")
    elif (computer == 0 or you == 1):
        print("RESULT: YOU LOOSE!")
    elif (computer == 0 or you == -1):
        print("RESULT: YOU WIN!")
    else:
        print("SOMETHING WENT WRONG!")


