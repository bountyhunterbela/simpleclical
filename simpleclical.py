def cli_cal(a,operation,b):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    else:
        if b!=0:
            return a/b
        else:
            return "Divesion by zero is impossible!"

while True:
    print("1.Enter calcultor\n2.Exit.")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=float(input("Enter your first number:"))
        operation=str(input("Enter your operation type,only(+,-,*,/):"))
        b=float(input("Enter your second number:")) 
        if operation in "+-*/":
            print(cli_cal(a,operation,b))
        else:
            print(f"Enter the right operation!") 
    elif choice==2:
        print(f"Exiting the program......")  
        break 
    else:
        print(f"Invalid choice!")

    
   