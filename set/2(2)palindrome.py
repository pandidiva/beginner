a=int(input("Enter number:"))
t=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(t==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
