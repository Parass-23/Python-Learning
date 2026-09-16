# try:
#     n=int(input("Enter a number: "))
#     print(100/n)
# except:
#     print("Invalid input. Please enter a valid integer.")
#cathing specific error
# try:
#     n=int(input("Enter a number: "))
#     print(100/n)    
# except Exception as e:#parent class of exceptions
#     print("Invalid input. Please enter a valid integer.")
#     print("Error details:", str(e))
    #-------------------------------------------------------
try:
    n=int(input("Enter a number: "))
    print(100/n)
    a=[1,2,3]
    print(a[5])#index error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")   
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)
# except IndexError:
#     print("error")