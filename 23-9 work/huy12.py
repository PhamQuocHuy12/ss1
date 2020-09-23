a = int(input("Please input here: "))         ##user input here
b = str(a)                                    ##covert a into string
c= 0                                          ## c is sum of all digit in a
for i in range (len(b)):
    c += int(b[i])
print(c)

# print(sum(list(map(int, list(str(input()))))))
