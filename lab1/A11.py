decVal = 41
binVal = bin(decVal)
shiftLeft1 = decVal << 1 & 0xff
shiftLeft2 = decVal << 2 & 0xff
shiftRight1 = decVal >> 1 & 0xff
shiftRight2 = decVal >> 2 & 0xff

print("Decimal form:\t", decVal)
print("Binary form:\t", binVal[2:10].rjust(8, '0'))
print("Shift Left (1):\t", shiftLeft1, "\t", bin(shiftLeft1)[2:10].rjust(8, '0'))
print("Shift Left (2):\t", shiftLeft2, "\t", bin(shiftLeft2)[2:10].rjust(8, '0'))
print("Shift right (1):\t", shiftRight1, "\t", bin(shiftRight1)[2:].rjust(8, '0'))
print("Shift right (2):\t", shiftRight2, "\t", bin(shiftRight2)[2:10].rjust(8, '0'))

