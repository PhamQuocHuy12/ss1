def recommend(userList, bookList):
    userName = input("Input the user here")
    try:
        if userName in userList:
            rate = dict[userName]
            print("User:" + userName)
            for i in range(len(rate)):
                print("Book: " + str(bookList[i]) + "  |Rate: " + str(rate[i]))
    except Exception as e:
        print(e)
        print('User not available! Please try again!')
        averages(bookList)

def averages(bookList):
    avg = [0] * len(bookList)
    for x in dict:
        zipped = zip(avg, dict[x])
        avg = [x + y for (x,y) in zipped]
    print(bookList)
    print(avg)
    for i in range(len(avg)):
        print("Book: " + str(bookList[i]) + "  |Rate: " + str(avg[i]))




if __name__ == "__main__":
    file = []
    with open("ratings-small.txt", 'r') as reader:
        for line in reader:
            file.append(line.split('\n')[0])
    print(file)


    bookList = []
    count = 1
    while count < len(file):
        bookList.append(file[count])
        count += 3
    bookList = list(dict.fromkeys(bookList))
    print(bookList)


    userList = []
    count = 0
    while count < len(file):
        userList.append(file[count])
        count += 3
    userList = list(dict.fromkeys(userList))
    print(userList)


    dict = {user : [0]*len(bookList) for user in userList}
    print(dict)


    # for element in file:
    #     if element in userList:
    #         index = file.index(element)
    #         bookIndex = bookList.index(file[index +1])
    #         print(index)
    #         print(bookIndex)
    #         rate_point = int(file[index + 2])
    #         print(rate_point)
    #         print("--------------")
    #         dict[element][bookIndex] += rate_point
    # print(dict)

    for i in range(len(file)):
        if file[i] in userList:
            index = i
            bookIndex = bookList.index(file[index +1])
            print(index)
            print(bookIndex)
            rate_point = int(file[index + 2])
            print(rate_point)
            print("--------------")
            dict[file[i]][bookIndex] += rate_point
    print(dict)


    print("Welcome to the CSC110 Book recommendatior, type the word in the \n"
          "left column to to the action.\n"
          "recommend: recommend the books for paricular user\n"
          "averages: output the average ratings of all books in the system\n"
          "quit: exit\n"
          "next task ?")
    command = input()
    print("next task ?")
    if command == "recommend":
        recommend(userList, bookList)
    if command == "averages":
        averages(bookList)


