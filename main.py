import math

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if not n%i:
            return False
    return True

def main():
    prime_list=[]
    for i in range(100001):
        if isPrime(i):
            prime_list.append(i)
    return prime_list
