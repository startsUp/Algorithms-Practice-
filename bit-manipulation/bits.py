def getBit(num, i):
    return (num & (1 << i)) != 0

def setBit(num, i):
    num |= (1 << i)
    return num

def clearBit(num, i):
    # mask and clear
    mask = ~(1 << i)
    return num & mask

print(getBit(3, 1))
print(setBit(3, 0)) 
print(clearBit(3, 0)) 
