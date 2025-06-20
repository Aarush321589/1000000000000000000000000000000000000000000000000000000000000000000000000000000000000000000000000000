try:
    num=int(input("enter a number"))
    print("the entered number is ",num)
except ValueError as ex:
    print("exception",ex)
    