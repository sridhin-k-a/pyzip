#program to calculate the areaa of aa trangle whose 3 sides are given

a=input("enter first side")#the value of first side a recive from user
b=input("enter second side")#the value of second side a recive from user
c=input("enter third side")#the value of third side a recive from user
s=(a+b+c)/2#calculate s
ar=(s*(s-a)*(s-b)*(s-c)**(.5))#calculate rea of trangle ar
print "area=",ar#display the area of the trangle