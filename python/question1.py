
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

def is_value_exist_in_matrix(sorted_matrix, target):
    for row in sorted_matrix:
        for col in row:
            if col > target:
                return False
            
            elif col == target:
                return True
    return False

print(is_value_exist_in_matrix(matrix, 9)) #False
print(is_value_exist_in_matrix(matrix, 10)) #True