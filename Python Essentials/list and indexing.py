marks = [90, 86, 95, 83, 70]#list(storage of data)
#  marks[0]=91
# print(marks[0])#indexing(starts with 0)
n=len(marks)
# for i in range(n):
#     print(marks[i])
#OR
# for elem in marks:
#     print(elem)
#--------------------------------------------------------
# for i in range(n):
#     if i%2==0:
#         print(marks[i])
#------------------------------------------------------
for i in range(n):
    if marks[i]%2==0:
        print(marks[i])
#-----------------------------------------------------------
# marks=[65,75,85]
# total=0
# for m in marks:
#     if m>=70:
#         total+=m
    
# print(total)
#-----------------------------------------------
# names=["amit","reha","aditya"]
# longest=names[0]
# for name in names:
#     if len(name)>len(longest):
#         longest=name
# print(longest)
#-------------------------------------------------
# data=[10,20,30]
# for i in range(len(data)):
#     data[i]=data[i]+10
# print(max(data))
# print(min(data))
#-----------------------------------------------------
# marks=[65,75,85]
# total=0
# for m in marks:
#     if m>=70:
#         total+=m
    
# print(total)