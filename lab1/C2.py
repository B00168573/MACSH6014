from math import sqrt

def checkIsPrime(num):
    if (num > 1):
        for a in range(2, int(sqrt(num)) + 1):
            if (num % a == 0):
                return False

        return True
    else:
        return False

def cipherFunc(baseNum, powerNum, modNum):
    checkPrimeResult = checkIsPrime(modNum)
    finalResult = pow(baseNum, powerNum) % modNum
    print("Is number \t", modNum, " a prime number? \t", checkPrimeResult)
    print("Result of (\t ", baseNum, " to the power of \t", powerNum, ") then mod by \t", modNum, " is \t", finalResult)
    return finalResult

finalResult = cipherFunc(8, 5, 269)
print("Is the result of (8 to the power of 5) equal to 219? \t", finalResult == 219)

