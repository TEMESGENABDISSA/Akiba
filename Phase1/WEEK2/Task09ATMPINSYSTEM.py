correctpin=1234
Counter=0;
while Counter<3:
    password=int(input("Enter your password"))
    if  correctpin==password:
        print(" sucessfully logged")
        break
    else:
        Counter = Counter+1
        print( f"Incorrect PIN  {3-Counter} Attempts remaining")
        if Counter==3:
            print("blocked")
