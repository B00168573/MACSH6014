import math

def isPrime(num):
    max = int(math.sqrt(num)) + 1

    if num % 2 == 0 or num % 3 == 0:
        return False

    for n in range(1, max):

        tmpNum = 6 * n + 1
        tmpNum2 = 6 * n - 1
        if tmpNum > max or tmpNum2 > max:
            break

        if num % tmpNum == 0 or num % tmpNum2:
            return False
    return True

foundedPrimeNum = []
for n in range(1, 100):
    if isPrime(n):
        foundedPrimeNum.append(n)
print("All prime numbers up to 100 by using 6k +/- 1: \t", foundedPrimeNum)
