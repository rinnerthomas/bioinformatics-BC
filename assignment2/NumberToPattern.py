index=45
k=4
index2=5353
k2=7

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
    
def NumberToPattern(index,k):
    if k==1:
        return NumberToSymbol(index)
    prefixindex=index // 4
    r=index % 4
    symbol=NumberToSymbol(r)
    return NumberToPattern(prefixindex,k-1) + symbol

print(NumberToPattern(index,k))
print(NumberToPattern(index2,k2))
