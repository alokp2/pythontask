"""
Welcome to IPL

 CSK , KIXP , KKR , RR , RCB

 YOUR NAME :   CSK
Opp. Team :  Automatically Select (Random)


------------------------------------------
 TOSS TIME :

 YOUR CHOICE : (H/T)  : H

 SYSTEM TOSS : H

 YOU WON THE TOSS

 SELECT YOUR CHOICE :

  1) BAT
 2) BOLL
 1) BAT
  6 - balls

1, 2 , 3 , 4 , 6 , WICKET , NO BALL , WIDE

"""







import random
print("Welcome to IPL")
li = ["CSK", "KIXP", "KKR", "RR", "RCB", "GT", "MI"]
print(li)
user = input("Your Name: ")
oppTeam = random.choice(li)
print("Opposite Team:", oppTeam)

'''Toss Time'''

user1 = input("Your CHOICE: (H/T):")
System_toss = random.choice(["H", "T"])
print("System_toss:", System_toss)

if user1 == System_toss:
    print("You Won the Toss")
    choice = int(input("Select Your Choice(Bat/Ball):"))
    if choice == 1:
        print("Bat")
    elif choice == 2:
        print("Ball")
    else:
        print("This is an invalid number")
else:
    print(random.choice(["Bat", "Ball"]))

# The possibility of getting all outcome in six balls
sum=0;
total_balls = [0, 1, 2, 3, 4, 5, 6, 'wicket', 'NoBall', 'wide']
n = 6
for items in range(n):
    print(random.choice(total_balls), end=" ")
