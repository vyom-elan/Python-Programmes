'''When each digit of a given number are seperated, raised to the power of their respective position
    and added then if the sum is equal to the given number the number is said to be a disarium number.
    For example - 175= 1^1+7^2+5^3=175'''
def le(n):      #fn to get the length of the number
    ln=0;
    while(n!=0):
        ln=ln+1;                            
        n=n//10;
    return ln;
num=int(input("Enter the number you want to checl"));
rem=sum1=0;
len1=le(num);                   #calling fn
num1=num;
while(num>>0):
    rem=num%10;         #to get the last digit each time
    sum1=sum1+int(rem**len1);
    num=num//10;
    len1=len1-1;        #decrementing counter till we reach the last digit

if(sum1==num1):
    print(str(num1)+" is a disarium number");
else:
    print(str(num1)+" is not a disarium number");
