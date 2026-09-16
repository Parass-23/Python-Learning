student={
    "name": "paras",
    "age" : 18,
    "city" : "panvel",
    "state":"maharastra"


}
for k in student.keys(): #-->print(access) all the keys
    print(k)
#-------------------------------------
for v in student.values():#--print(access) all the values
    print(v)
#OR for acessing values
# for k in student.keys():
#     print(student[k])
#--------------------------------------
for elem in student.items(): #-->gives you tupple('key','value')
    print(elem)
    