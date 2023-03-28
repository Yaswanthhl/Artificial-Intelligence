rows1 = int(input("Enter number of rows in matrix 1: "))
cols1 = int(input("Enter number of columns in matrix 1: "))

rows2 = int(input("Enter number of rows in matrix 2: "))
cols2 = int(input("Enter number of columns in matrix 2: "))

if rows1 == rows2 and cols1 == cols2:
    matrix1 = []
    print("Enter the elements of matrix 1: ")
    for i in range(rows1):
        element=[int(x) for x in input().split()]
        matrix1.append(element)

    matrix2 = []
    print("Enter the elements of matrix 2: ")
    for i in range(rows2):
        element=[int(x) for x in input().split()]
        matrix2.append(element)
        
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            sum = matrix1[i][j] + matrix2[i][j]
            row.append(sum)
        result.append(row)
    print("Result: ")
    for row in result:
        print(row)

else:
    print("Matrix Addition is Impossible as Rows & Columns are Not Identical")