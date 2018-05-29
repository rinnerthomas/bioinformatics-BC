text="AGT"
text2="CTTCTCACGTACAACAAAATC"

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

print(PatternToNumber(text))
print(PatternToNumber(text2))