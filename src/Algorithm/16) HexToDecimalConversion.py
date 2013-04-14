def convertCharToDecimal(ch):
    if 'A' <= ch <= "F":
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')

def convertHexToDecimal(hex):
    decimalNumber = 0
    for ch in hex:
       # print(ch)
        if 'A' <= ch <= 'F' or '0' <= ch <= '9':
            decimalNumber = decimalNumber * 16 + convertCharToDecimal(ch)
        else:
            return None
    print(decimalNumber)
    return decimalNumber

convertHexToDecimal("ABBC")
convertHexToDecimal("AF71")
convertHexToDecimal("ax71")