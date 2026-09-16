#to filter out who satisfys the conditions
#for ex
# num=[1,2,3,4,5,6]
# even=[]
# for elem in  num:
#     if elem%2==0:
#         even.append(elem)
# print(even)
#----------------------------------------
#by using filter
#syntax is same like map
num=[1,2,3,4,5,6,7,8]
even=list(filter(lambda x:x%2==0,num))
print(even)
#or
even=list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8]))
print(even)
#or
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8])))
