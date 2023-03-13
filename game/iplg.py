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

total_balls = [0, 1, 2, 3, 4, 5, 6, 'WICKET', 'NoBALL', 'Wide']
print(type(total_balls))
for items in total_balls:
    print(items)
