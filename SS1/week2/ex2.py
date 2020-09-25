
def DateForm(date: list):
    form = ""
    monthList = {"1": "January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"NovemBer", "12":"December",}
    form += monthList[date[0]] + ", "
    dayList = { "1":"st", "2":"nd", "3":"rd", "11":"st", "12":"nd", "13":"rd", "21":"st", "22":"nd", "23":"rd", "31":"st"}
    if date[1] == 1 or date[1] == 2 or date[1] == 3 or date[1] == 11 or date[1] == 12 or date[1] == 13 or date[1] == 21 or date[1] == 22 or date[1] == 23 or date[1] == 31:
        form += date[1] + dayList[str(date[1])] + ", "
    else:
        form += date[1] + "th" + ", "
    form += date[2]
    return form
def validateDay(day: str, month: str):
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month)==7 or int(month) ==8 or int(month) == 10 or int(month) == 12:
        if 1 <= int(day) <= 31:
            return True
    if int (month) == 2:
        if 1<= int(day)<= 28:
            return True
    else:
        if 1<= int(day)<=30:
            return True
def validateYear(year: str):
    if int(year) > 0 :
        return True
def validateMonth(month: str):
    if 1 <= int(month) <= 12:
        return True
if __name__ == "__main__":
    validate = False
    while not validate:
        date= str(input("Input date here: "))
        arrDate = list(date.split("/"))
        # print(validateDay(arr))
        # print(validateYear())
        # print(validateMonth())
        if validateMonth(arrDate[0]) == True and validateDay(arrDate[1], arrDate[0]) == True and validateYear(arrDate[2]) == True:
            validate = True
        else:
            print("Invalid Input ! Please try again!")
    if validate:
        print (DateForm(arrDate))

