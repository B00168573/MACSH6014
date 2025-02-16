from math import sqrt

def checkIsPrime(num):
    if (num > 1):
        for a in range(2, int(sqrt(num)) + 1):
            if (num % a == 0):
                return False

        return True
    else:
        return False

def cipherFunc(baseNum, powerNum, modNum, expectedNum):
    checkPrimeResult = checkIsPrime(modNum)
    finalResult = pow(baseNum, powerNum) % modNum
    print("Is number \t", modNum, " a prime number? \t", checkPrimeResult)
    print("Result of (\t ", baseNum, " to the power of \t", powerNum, ") then mod by \t", modNum, " is \t", finalResult)
    print("Is the result of (\t", baseNum, " to the power of \t", powerNum, ") then mod by \t", modNum, " equals to \t",
          expectedNum, "? \t", finalResult == expectedNum)
    return finalResult

message = input('Enter message: ')
e = input('Enter exponent: ')
p = input('Enter prime: ')
ans = input('Enter expected answer: ')
cipher = cipherFunc(int(message), int(e), int(p), int(ans))


