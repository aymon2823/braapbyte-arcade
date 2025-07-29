print ("Welcome to my Dirt Bike quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)") 
score =  0 

answer = input("What should you always check before you ride? ")
if answer.lower() == "gas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Try again!")
    



answer = input("What should you always pack before you ride? ")
if answer.lower() == "gear bag":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Try again!")
    


answer = input("What should you always check before you ride? ")
if answer.lower() == "oil":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Try again!")
    


answer = input("What should you always pack before you ride? ")
if answer.lower() == "knee pads":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Try again!")
    

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4) * 100) + "%.")


