marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got an A grade.")
elif marks >= 75 and marks < 90:
    print("You got a B grade.")
elif marks >= 60 and marks < 75:
    print("You got a C grade.")
elif marks >= 40 and marks < 60:
    print("You got a D grade.")
else:
    print("You failed the exam.")