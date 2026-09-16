# with elif
#-----------------------------------------------

# marks=int(input("Enter your marks: "))
# if marks < 30:
#     print("fail")
# elif marks >= 30 and marks < 50:
#     print("pass")
# elif marks >= 50 and marks < 70:
#     print("second class")
# elif marks >= 70 and marks < 90:
#     print("first class")
# else:
#     print("distinction")

#coolest code
marks=int(input("Enter your marks: "))
if marks < 30:
    print("fail")
elif marks <= 50:  # if marks is not  less than 30 then if conditionis wrong then automatically 
    print("pass") #it is clear that  it  grater than 30 so we do  not needto write the (and wala stuff "hindi")
elif marks <= 70: #so this  thing can be avoid and that i  havewritten the coolest code without this thing.
    print("second class")
elif marks <= 90:
    print("first class")
else:
    print("distinction")



#-----------------------------------------------------
# without elif

#----------------------------------------------------
# marks =int(input("Enter your marks: "))
# if marks < 30:
#     print("fail")
# else:
#     if marks >= 30 and marks < 50:
#         print("pass")
#     else:
#         if marks >= 50 and marks < 70:
#             print("second class")
#         else:
#             if marks >= 70 and marks < 90:
#                 print("first class")
#             else:
#                 print("distinction")



