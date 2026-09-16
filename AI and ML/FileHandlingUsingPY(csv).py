#csv-->comma seperated values.

#csv
import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","marks","city"])
    writer.writerow(["paras","95","mumbai"])
    writer.writerow(["raj","90","delhi"])
with open("student.csv","r",newline="") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#----------------------------------------------------
name=input()
marks=int(input())
city=input()
with open("student.csv","a",newline="") as file:
    append=csv.(file)
    append.appendrow([name,marks,city])
    for row in append:
            print(row)


