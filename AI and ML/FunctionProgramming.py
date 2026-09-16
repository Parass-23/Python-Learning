n=[1,2,3,4,5]
# sq=[]
# for elem in n:
#     s.append(elem**2)
# print(s)
#----------mentos zindagi----------
#using function programming

# sq=list(map(lambda x: x**2,n))
# print(sq)

#-----------------------------------------
#lambda functions-->anonymous func
#syntax---> lambda parameters :operations

# def sq(x):
#     return x*x
# print(sq(5))
#or
sq=lambda x:x*x
print(sq(5))

#----------------------------------
tw=lambda x:2*x
print(tw(10))
#--------------------------------
sum=lambda x,y:x+y
print(sum(2,5))
#----------------------------
# def mx(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(mx(2,3))
#or
# mx=lambda a,b:max(a,b)
mx=lambda a,b :a if a>b else b
print(mx(5,8))
#---------------------------------
def num(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
print(num(5))
#--or--
check1=lambda n: "even" if n%2==0 else 'odd'
print(check1(4))
#--------------------------------------
check2=lambda n: n[-1]
print(check2("paras"))
#------------------------------------
# def mul(a,b,c):
#     return a*b*c
# print(mul(1,2,3))
#-----Or--------
mul= lambda x,y,z : x*y*z
print(mul(3,2,1))