# Start with a positive number replace until it return single digit which is recursive sum of the digits in number
def happy(n):
    sum=0
    while n!=0:
        d=n%10
        sum+=d
        n//=10
    #Check if sum is single digit
    check=sum//10
    if check == 0:
        return sum
    else:
     return happy(sum)
n=int(input("Enter the number : "))
digit=happy(n)
print("Happy number is : ",digit)