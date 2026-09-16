students=[{'roll':101,'name':'paras','age':18,'course':'python','marks':90},
          {'roll':102,'name':'purva','age':49,'course':'python','marks':80},
          {'roll':103,'name':'pramod','age':46,'course':'aiml','marks':75},
          {'roll':104,'name':'alex','age':19,'course':'aiml','marks':60},
          {'roll':105,'name':'ryan','age':21,'course':'python','marks':35}
          ]
# for student in students:
#     print(student["name"])

# sum=0
# for student in students:
#     sum+=student["marks"]
# print(sum)

# sum=0
# for student in students:
#     sum+=student["marks"]
# print(sum/len(students))

# count=0
# for student in students:
#     if student["marks"]>40:
#         count+=1
# print(count)

# def calc_grade(marks):
#     if marks>=90:
#         grade="A"
#     elif marks>=75:
#         grade="B"
#     elif marks>=60:
#         grade="c"
#     else:
#         grade="D"
#     return grade
# for student in students:
#     print(calc_grade(student["marks"]))


# def search(rollno):
#     found=False
#     for student in students:
#         if student["roll"]==rollno:
#             print(student)
#             found=True
#             break

#     return found
        
# roll=int(input("enter roll no : "))
# search(roll)

# name=input("enter name")

# for student in students:
#     if student['name'].lower()==name.lower():
#            print(student)

# def search(students):
#     maxmarks=0
#     for student in students:
#         if student['marks']>maxmarks:
#             maxmarks=student['marks']
#             topper=student

#     return topper
# print(search(students))

# courses={}
# for student in students:
#     if student['course'] not in courses:
#         courses[student['course']]=1
#     else:
#         courses[student['course']]+=1

# print(courses)

# courses=[]
# for student in students:
#     courses.append(student['course'])

# print(courses)
# s=set(courses)
# print(s)

# class student:
#     def __init__(self,roll,name,age,course,marks):
#         self.roll=roll
#         self.name=name
#         self.age=age
#         self.course=course
#         self.marks=marks
#     def show(self):
#         print(self.roll,self.name,self.age,self.course,self.marks)

# s1=student(106,"paras",18,"python",100)
# s1.show()

def search(rollno):
    found=False
    for student in students:
        if student["roll"]==rollno:
            print(student)
            found=True
            break

    return found
        


def top(students):
    maxmarks=0
    for student in students:
        if student['marks']>maxmarks:
            maxmarks=student['marks']
            topper=student

    return topper


a = int(input("1.Display\n2.Search\n3.Average\n4.Topper\n5.Exit\nEnter choice: "))

if a == 1:
    for student in students:
        print(student)

elif a == 2:
    roll = int(input("Enter roll no: "))
    search(roll)

elif a == 3:
    total = 0
    for student in students:
        total += student["marks"]
    print("Average =", total / len(students))

elif a == 4:
    print(top(students))

elif a == 5:
    print("Thank you")

else:
    print("Invalid choice")
    

        







 