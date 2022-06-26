def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if(num%n==0):
            return False;
    return True;

def gcd(num1,num2):
    while(num2):
        num1, num2 = num2, num1 % num2;
    return num1;

def lcm(num1, num2):
    return (num1*num2)//gcd(num1,num2);
