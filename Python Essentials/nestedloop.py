# for j in range(5):
#     for i in range(4):
#         print("*",end=" ")
#     print()
#-----------------------------------------------
# for i in range(1,6):
#     for j in range(4):
#         print(i, end=" ")

#     print()
#-----------------------------------------------------
for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()
#---------------------------------------------------
# for i in range(3):
#     for j in range(10,50,10):
#         print(j,end=" ")
#     print()
#-------------------------------------------------
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#---------------------------------------------------------
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
#--------------------------------------------------
for i in range(1,6):

    for j in range(1,i+1):
        print(j,end=" ")

    print()
#----------------------------------------------------
i=1
for row in range(1,5):

    for col in range(row):
        print(i,end=" ")
        i=i+1

    print()