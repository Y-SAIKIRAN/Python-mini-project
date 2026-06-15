import random

Target=random.randint(1,100)

while True:
    userChoice =input("Guess the number or Quit: ")
    if userChoice.lower() == 'quit':
        break

    if not userChoice.isdigit():
        print("Enter numbers only")
        continue

    userChoice=int(userChoice)    
    if (userChoice==Target):
        print("CONGRATULATIONS YOU ARE CORRECT")
        break

    elif (userChoice<Target):
        print("Your number was smaller than the target, think bigger")
    else:
        print("Your number was bigger than the target, think smaller")

print()
print("----GAME OVER----")
