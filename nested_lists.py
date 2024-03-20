matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

# first_row_first_column=matrix[0][0]
# print(first_row_first_column)

# for row in matrix:
#     print(row)

for row in matrix:
    print(' '.join(map(str,row)))
