# Input callbacks

def getInputFromChinese() -> str:
    pass

def getInputFromEnglish() -> str:
    pass

def getInputFromTerminal() -> str:
    text = input()
    return text

# Output callbacks

def printInput(strIn: str):
    print(strIn)

def outputInputEnglish(strIn: str):
    pass

def outputInputChinese(strIn: str):
    pass