#Asking the user to input a number, check if its prime and return the result
def isPrime(num):
    for i in range(2,int(num**0.5)+1):#taking the square root of the number instead of using the whole number to reduce the number of iterations

        if num%i == 0:#Dividing the square root gotten above by values between 2 and the number
            return False
        else:
            return True
n = int(input("Enter any value"))
if isPrime(n):
    print(f"")