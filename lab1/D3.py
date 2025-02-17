import sys

maxVal = 1000
if len(sys.argv) > 1:
    maxVal = int(sys.argv[1])

def findPrimesUpTo(num):
    size = num // 2
    sieve = [1] * size
    limit = int(num ** 0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = (2 * i) + 1
            tmp = ((size - 1) - i) // val
            sieve[i+val::val] = [0] * tmp
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

scopes = [100, 1000, 5000, 10000]\

for n in range(0, len(scopes)):
    allPrimes = findPrimesUpTo(scopes[n])
    print("The biggest prime number found under the max value \t", scopes[n], " is: \t", allPrimes[-1])