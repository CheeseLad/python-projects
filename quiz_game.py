print("Welcome to my Python quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Lets go!")

ans = input('What is the Python syntax for "not-equals"? ')
if ans == "!=":
    print("Correct!")