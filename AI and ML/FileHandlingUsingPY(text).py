#most commonly used types of files in aiml-->text,csv

#testfile
#syntax--> file=open(filename,folder)
file=open("sample.txt","w")
file.write("paras\n")
file.write("purva\n")
file.write("pramod\n")
file.close()
file=open("sample.txt","r")
data=file.read()#it reads all lines (i.e text)
#data=file.readline() #it reads one line(i.e all things is printed before pressing enter after first line)
# data=file.readlines()#it reads all line and stires it in list
print(data)
file.close()
#--------------------------
# for line in data:
#     print(line)
#or
# file=open("sample.txt","r")
# for line in file:
#     print(line,end="")
# file.close()
#--------------------------------------------
# #w-->write mode
# #r-->read mode
# #a-->append mode
# file=open("sample.txt","a")
# file.write("rudra")
# file.close()
# file=open("sample.txt","r")
# for line in file:
#     print(line)
# file.close()
#-------------------------------------
# file=open("abc.txt","x")#it just creats a file and stores , it is empty
# file.close()
#----------------------------------------
with open("sample.txt","r") as file:
    print(file.read())
    #this is the more standerd way of file handling and ther is no need for closing the file.
#another file
with open("demo.txt","w") as file:
    file.write("aditya")
with open("demo.txt","a") as file:
    file.write("\nparas")
with open("demo.txt","r") as file:
    print(file.read())
    