rows, cols = (int(input(("Input number of rows: "))), int(input("Input the number of columms:  ")))
arr = [[0 for x in range(cols)] for y in range(rows)]
for i in range (rows):
    for j in range (cols):
        arr[i][j]= i*j
print(arr)