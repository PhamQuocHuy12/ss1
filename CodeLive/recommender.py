def recommend(userList, bookList):
    userName = input("Input the user here")
    try:
        if userName in userList:
            rate = dict[userName]
            print("User:" + userName)
            for i in range(len(rate)):
                print("Book: " + str(bookList[i]) + "  |Rate: " + str(rate[i]))
        else:
            averages(userList,bookList)
    except Exception as e:
        print(e)
        print('User not available! Please try again!')
        

def averages(userList , bookList):
    book_rate = []
    for book in bookList:
        index = bookList.index(book)
        count = 0
        avg = 0
        for x in dict:
            avg += dict[x][index]
            if dict[x][index] != 0:
                count+=1
        avg = avg/ count
        book_rate.append([book, avg])
        print("Book: " + str(book) + "  |Rate: " + str(avg))

    sorted(book_rate, key=lambda x: x[1])
    print(book_rate)
    print("em dang sort do thay a")


if __name__ == "__main__":
    # READ FILE -------------------------------------------------------------------------
    file = []
    with open("ratings-small.txt", 'r') as reader:
        for line in reader:
            file.append(line.split('\n')[0])

    # CREATE BOOK LIST ------------------------------------------------------------------
    bookList = []
    count = 1
    while count < len(file):
        bookList.append(file[count])
        count += 3
    bookList = list(dict.fromkeys(bookList))

    #CREATE USER LIST ------------------------------------------------------------------
    userList = []
    count = 0
    while count < len(file):
        userList.append(file[count])
        count += 3
    userList = list(dict.fromkeys(userList))

    # GENERATE DICT -------------------------------------------------------------------
    dict = {user : [0]*len(bookList) for user in userList}

    for i in range(len(file)):
        if file[i] in userList:
            index = i
            bookIndex = bookList.index(file[index +1])
            rate_point = int(file[index + 2])
            dict[file[i]][bookIndex] += rate_point

    # MAIN --------------------------------------------------------------------------
    print("Welcome to the CSC110 Book recommendatior, type the word in the \n"
          "left column to to the action.\n"
          "recommend: recommend the books for paricular user\n"
          "averages: output the average ratings of all books in the system\n"
          "quit: exit\n")
    eXit = False
    while(eXit == False):
        command = input()

        if command == "recommend":
            recommend(userList, bookList)
            print("next task ?")
        if command == "averages":
            averages(userList, bookList)
            print("next task ?")
        if command== "exit":
            eXit = True
            print("goodbye")


