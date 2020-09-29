def saddle_points(matrix):
    lst = []
    for row_number in range(len(matrix)):
        temp = 0
        for column_number in range(len(matrix[row_number])):
            if temp <= matrix[row_number][column_number]:
                temp = matrix[row_number][column_number]
                lst.append(temp)
        temp = 0

    print(lst)

    for i in range(len(matrix)):
        l = max(matrix[i])
        print((i , matrix[i].index(l)))

    
    transpouse = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for j in transpouse:
        o = min(j)
        for i in range(len(matrix)):
            print(i, matrix[i].index(o))


