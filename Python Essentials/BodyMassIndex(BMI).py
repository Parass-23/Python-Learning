bmi=float(input("Enter your BMI(Body Mass Index): "))
if bmi<18.5:
    print("You are underweight.")
elif bmi>=18.5 and bmi<24.9:
    print("You are normal weight.")
elif bmi>=25 and bmi<29.9:
    print("You are overweight.")
elif bmi>=30 and bmi<34.9: 
    print("You are obese class 1.")
elif bmi>=35 and bmi<39.9:
    print("You are obese class 2.")
else:
    print("You are extremely obese.")