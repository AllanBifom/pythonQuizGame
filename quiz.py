# Allan Bifom
# Short python quiz Game

print("Welcome to Quiz Game! ")

playing = input("Are you ready to play?(Y/N) ").lower()
if playing != "y" and playing != "yes":
    print("Exiting game...")
    quit()

print("Okay lets Get started ;)")

score = 0
name = input("Enter your name? ")

print("ok "+ name + " lets begin")

answer = input("What does ALU stand for? ").lower()
if answer == "arithemetic and logical unit":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "Random access memory" or answer =="random access memory":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What is 100 base 2(binary) in base 10? ").lower()
if answer == "4" or answer =="four":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("in terms of networking, what does LAN stand for? ").lower()
if answer == "local area network":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    score += 1
    print("correct!")
else :
    print("Incorrect!")

print("Well done "+ name + " you scored " + str(score) +"/8")
