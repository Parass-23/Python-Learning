s1=set()
s2=set()
for i in range(3):
    m=input("enter 3 subs of student one: ")
    s1.add(m)
for j in range(3):
    m=input("enter 3 subjects of student 2: ")
    s2.add(m)


print(s1 & s2)
print(s1-s2)
print(s2-s1)

