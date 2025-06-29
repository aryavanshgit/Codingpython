name = input("What is your name?\n")
age = int(input("what is your age?\n"))
gender = input ("What is your gender?\n")
achievment = input("What is your achievment?\n")


if age >=18:
    print("You are adult.")

if age >=13 and age <18:
    print("You are a teenager.")

if age >=0 and age <13:
    print("You are a kid.")


print("Congratulations for your achievment", achievment)


if age >=0 and age <7:
    exit()

if age >=7:
    print("\nYou are eligible for the quiz.")

quizyesno = str(input("If you want to start the Quiz type Yes else type No.")) 


if quizyesno == "No":
    print("Ok Bye.")

if quizyesno == "No":
    exit()

if quizyesno == "Yes":
    print("Let's Start.")

print("There would be point system in the game. Point would be out of 50. 5 Questions 10 points per correct answer.")

point = 0


a = input("Who is the CEO of Microsoft?")
if a == "Satya Nadella":
    print("Correct answer ")    
    point+=1


else:
    print("Wrong Answer")
    point+=1

b = input("Who is the President of USA? ")
if b =="Donald Trump":
    print("Correct answer")
    point+=1

else:
    print("Wrong Answer")

c = input("Who created Apple?")
if c =="Steve Jobs":
    print("Correct Answer")
    point+=1

else:
    print("Wrong Answer")

d = input("Who is The Prime Minester of India?")
if d =="Narendra Modi":
    print("Correct Answer")
    point+=1

else:
    print("Wrong Answer")

e = input("Full form of UPI.")
if e == "Unified Payment Interface":
    print("Correct Answer")
    point+=1

else:
    print("Wrong Answer")


print(point, "is your score \n")

print("See you soon Bye")

exit() 