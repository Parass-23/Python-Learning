set={1,2,3,4,5,6,6}
print(len(set))#it sutomaticall removes the duplicate value(i.e only unique elem is stored)
fruit={"banana","mango","apple","mango"}
print(fruit)
#major diff btw dict and set is that dict is key value pairs and set are single elem
#set are mutable
#empty tuple syntax--->a=set()
#they are unordered(i.e not indexing)
set.add(10)#to add an elem in set
set.remove(6)#to remove an elem in set
# item=set.pop()#randomly remove elem as you run again and again
# set.clear()#rmove all the elements from the set(i.emakes empty set)
#print(A | B) #makes a union of 2 sets
#print(A & B) #makes intersection of two sets A and B
#print(A - B) #makes set difference
print(set,end=" ")




#-------------------------------------
# students=[
#     "rahul",
#     "paras",
#     "purva",
#     "pramod",
#     "purva",
#     "pramod",
# ]
# stu=[]
# for student in students:
#     if student not in stu:
#         stu.append(student)
# print(stu)

