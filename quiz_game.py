import os
os.system("cls")


print ("Welcome To Quiz Game Of Computer!")

play = input("Do you want to play? ")

if play.lower() != "yes":
      quit()

print("Let's play :)")
scorre = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
      print("Correct!")
      scorre +=1
else:
      print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
      print("Correct!")
      scorre +=1
else:
      print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
      print("Correct!")
      scorre +=1
else:
      print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
      print("Correct!")
      scorre +=1
else:
      print("Incorrect!")


print(f"You got {str(scorre)} question correct!")
print(f"You got {str((scorre / 4)*100)}%.")