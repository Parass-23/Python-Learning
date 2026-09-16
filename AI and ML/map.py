# def cube(lst):
#     cb=[]
#     for elem in lst:
#         cb.append(elem**3)
#     return cb
# print(cube([1,2,3]))
#---------------------------------
#map
#syntax-->map(function.iterable)-->it returns a map object
#------------------------
# lst=[4,6,2]
# cube =list(map(lambda x: x**3,lst))
# print(cube)
# #or
# cube =list(map(lambda x: x**3,[4,6,2]))
# print(cube)
# #or
# print(list(map(lambda x: x**3,[4,6,2])))
#-------------------------------------------------
#to plus 5 in every element inlist
# plus=[4,6,2]
# plu =list(map(lambda x: x+5,plus))
# print(plu)
# #or
# plu =list(map(lambda x: x+5,[4,6,2]))
# print(plu)
# #or
# print(list(map(lambda x: x+5,[4,6,2])))
#-----------------------------------------------
#convert strings inlist in uppercase
# def up(names):
#     upper=[]
#     for name in names:
#         upper.append(name.upper())
#     return upper
# ss=["purva","paras","pramod"]
# print(up(ss))
# #or
# ups=list(map(lambda s:s.upper(), ss))
# print(ups)

#--------------------------------------------------
#put prices list in new list  with adding 18% gst
def tax(g):
    gst=[]
    for elem in g:
        gst.append(elem*1.18)
    return gst
s=[100,200,250,150]
print(tax(s))
#or
tx=list(map(lambda x:x*1.18,s))
print(tx)
