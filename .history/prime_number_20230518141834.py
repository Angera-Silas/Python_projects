#Asking the user to input a number, check if its prime and return the result
def isPrime(num):
    for i in range(2,int(num**0.5)+1):#taking the square root o
        if num%i == 0:
            return False
        else:
            return True