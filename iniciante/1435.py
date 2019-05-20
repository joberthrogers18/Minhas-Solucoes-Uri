
def verification(matrix, size_matrix):
    
    for key in range(2):
        i = j = 0
        for i in range(size_matrix):

            for j in range(size_matrix):

                neighbor = []

                if i != 0 and j != 0  and i < size_matrix - 1 and j < size_matrix - 1:
                    if matrix[i][j + 1] is not 0:
                        neighbor.append(matrix[i][j + 1])
                    if matrix[i+ 1][j] is not 0:
                        neighbor.append(matrix[i + 1][j])
                    if matrix[i- 1][j] is not 0:    
                        neighbor.append(matrix[i - 1][j])
                    if matrix[i][j -1] is not 0:
                        neighbor.append(matrix[i][j - 1])
                    
                    matrix[i][j] = min(neighbor) + 1    
               
    return matrix

def show (matrix):
    
    string_matrix = ''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j != 0:
                string_matrix += '   ' + str(matrix[i][j])
            else:
                string_matrix += '  ' + str(matrix[i][j])

        string_matrix += '\n'

    return string_matrix

number_input = -1

while True:

    size_matrix = int(input())

    if (size_matrix == 0):
        break

    matrix = []
    cont = 0
    neighbor = []

    for i in range(size_matrix):
        aux = []
        for j in range(size_matrix):

            if i == 0 or j == 0  or i == size_matrix - 1 or j == size_matrix - 1:
                aux.append(1)
            else:
                aux.append(0)
        matrix.append(aux)


    new_matrix = show(verification(matrix, size_matrix))
    print(new_matrix)

