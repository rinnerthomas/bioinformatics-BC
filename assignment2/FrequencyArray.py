text="ACGCGGCTCTGAAA"
k=2

def SymbolToNumber(symbol):
    if symbol=="A":
        return 0
    if symbol=="C":
        return 1
    if symbol=="G":
        return 2
    if symbol=="T":
        return 3

def NumberToSymbol(number):
    if number == 0:
        return "A"
    if number == 1:
        return"C"
    if number == 2:
        return "G"
    if number == 3:
        return  "T"

def PatternToNumber(pattern):
    if pattern == "":
        return 0
    symbol=pattern[-1]
    prefix=pattern[0:len(pattern)-1]
    return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)

def NumberToPattern(index,k):
    if k==1:
        return NumberToSymbol(index)
    prefixindex=index // 4
    r=index % 4
    symbol=NumberToSymbol(r)
    return NumberToPattern(prefixindex,k-1) + symbol

def ComputingFrequencies(text, k):
    FREQUENCYARRAY=[0]*(4**k)
    for i in range (0,len(text)-1):
        pattern=text[i:i+k]
        j=PatternToNumber(pattern)
        FREQUENCYARRAY[j]=FREQUENCYARRAY[j]+1
    return FREQUENCYARRAY
            
print(ComputingFrequencies(text,k))




