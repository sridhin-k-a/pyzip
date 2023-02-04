#find the largest of three number

a=input("enter first number")#recive first number a from user
b=input("enter second number")#recive second number a from user
c=input("enter third number")#recive third number a from user
    if a>b:#check the number b less than a
        if a>c:#check the number c less than a
            print a,"is large"#display a is largen number

        else:
            print c,"is large"#display c is larger number
    else:
        if b>c:#check the number c less than b
            print b,"is large"#display b is larger number
        else:
            print c,"is large"#display c is larger number
