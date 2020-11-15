import random
rps = input("Please enter Rock, Paper or scissors (R/P/S): ")
while rps != "R" and rps != "P" and rps != "S" :
    rps = input("Invalid input. Please enter (R/P/S) :");

rnum = random.randint(1,3) # 1 = rock  2 = paper  3 = scissors

if rnum == 1:
    print("The computer picked R, you picked " , rps)
if rnum == 2:
    print("The computer picked P, you picked " , rps)
if rnum == 3:
    print("The computer picked S, you picked " , rps)

if rps == "R":
    if rnum == 1:
        print("It is a draw!")
    if rnum == 2:
        print("You lose!")
    if rnum == 3:
        print("You win!")

if rps == "P":
    if rnum == 1:
        print("You win!")
    if rnum == 2:
        print("It is a draw!")
    if rnum == 3:
        print("You lose!")

if rps == "S":
    if rnum == 1:
        print("You lose!")
    if rnum == 2:
        print("You win!")
    if rnum == 3:
        print("It is a draw!")


  
