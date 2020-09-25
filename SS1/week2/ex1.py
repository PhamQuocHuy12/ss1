def NameShortening(name):
    arrName = list(name.split())
    shortened = ""
    separatedName = ""
    for i in range(len(arrName)):
        separatedName = arrName[i]
        shortened += separatedName[0] + ". "
    return shortened
if __name__ == "__main__":
    name = str(input("Input ur name here: "))
    print(NameShortening(name))
