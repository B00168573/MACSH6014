def gcd(a, b):
    originalA = a
    originalB = b
    while(b != 0):
        remainder = a % b
        a = b
        b = remainder

    print("The greatest common divisor for \t", originalA, " and \t ", originalB, "is \t", a)
    return a

result1 = gcd(4105, 10)
result1 = gcd(4539, 6)