#Conditional statement

#Variable Declaration
num=int(input())

#Condition Statement
if(num%2!=0): # num is odd
    print("Weird")
    
elif(num%2==0 and 2<=num<=5): #num is even and range 2 to 5
    print("Not Weird")
    
elif(num%2==0 and 6<=num<=20): #num is even and range 6 to 20
    print("Weird")
    
elif(num%2==0 and num>20): #num is even and num 21 and above
    print("Not Weird")