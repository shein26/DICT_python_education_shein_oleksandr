def read_matrix():
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix, rows, cols


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def add_matrices(matrix_a, matrix_b, rows, cols):
    result_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result_matrix.append(row)
    return result_matrix


def multiply_matrix_by_constant(matrix, rows, cols, constant):
    result_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] * constant)
        result_matrix.append(row)
    return result_matrix


def multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, rows_b, cols_b):
    if cols_a != rows_b:
        print("The operation cannot be performed.")
        return None

    result_matrix = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell_value = 0
            for k in range(cols_a):
                cell_value += matrix_a[i][k] * matrix_b[k][j]
            row.append(cell_value)
        result_matrix.append(row)
    return result_matrix


def transpose_main_diagonal(matrix, rows, cols):
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed_matrix



def transpose_side_diagonal(matrix, rows, cols):
    transposed_matrix = [[matrix[cols - j - 1][rows - i - 1] for j in range(cols)] for i in range(rows)]
    return transposed_matrix

def transpose_vertical_line(matrix, rows, cols):
    transposed_matrix = [row[::-1] for row in matrix]
    return transposed_matrix


def transpose_horizontal_line(matrix, rows, cols):
    transposed_matrix = matrix[::-1]
    return transposed_matrix


def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            det += ((-1) ** j) * matrix[0][j] * determinant(minor(matrix, 0, j), n - 1)
        return det


def minor(matrix, row, col):
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]


# Функція для знаходження зворотної матриці
def inverse_matrix(matrix, n):
    det = determinant(matrix, n)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return None
    if n == 1:
        return [[1 / det]]
    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor_matrix = minor(matrix, i, j)
            cofactor = ((-1) ** (i + j)) * determinant(minor_matrix, n - 1)
            row.append(cofactor / det)
        cofactors.append(row)
    inverse = transpose_main_diagonal(cofactors, n, n)
    return inverse


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            print("Enter size of first matrix:")
            matrix_a, rows_a, cols_a = read_matrix()
            print("Enter first matrix:")
            matrix_b, rows_b, cols_b = read_matrix()

            if rows_a == rows_b and cols_a == cols_b:
                result = add_matrices(matrix_a, matrix_b, rows_a, cols_a)
                print("The result is:")
                print_matrix(result)
            else:
                print("The operation cannot be performed.")

        elif choice == "2":
            print("Enter size of matrix:")
            matrix, rows, cols = read_matrix()
            constant = float(input("Enter constant: "))
            result = multiply_matrix_by_constant(matrix, rows, cols, constant)
            print("The result is:")
            print_matrix(result)

        elif choice == "3":
            print("Enter size of first matrix:")
            matrix_a, rows_a, cols_a = read_matrix()
            print("Enter first matrix:")
            matrix_b, rows_b, cols_b = read_matrix()
            result = multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, rows_b, cols_b)
            if result is not None:
                print("The result is:")
                print_matrix(result)
        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            transpose_choice = input("Your choice: ")

            print("Enter matrix size:")
            rows, cols = map(int, input().split())
            print("Enter matrix:")
            matrix = [list(map(float, input().split())) for _ in range(rows)]

            if transpose_choice == "1":
                result = transpose_main_diagonal(matrix, rows, cols)
            elif transpose_choice == "2":
                result = transpose_side_diagonal(matrix, rows, cols)
            elif transpose_choice == "3":
                result = transpose_vertical_line(matrix, rows, cols)
            elif transpose_choice == "4":
                result = transpose_horizontal_line(matrix, rows, cols)

            print("The result is:")
            print_matrix(result)

        elif choice == "5":
            print("Enter matrix size:")
            n, m = map(int, input().split())
            if n != m:
                print("The operation cannot be performed. The matrix must be square.")
                continue
            print("Enter matrix:")
            matrix = [list(map(float, input().split())) for _ in range(n)]
            det = determinant(matrix, n)
            print("The result is:")
            print(det)

        elif choice == "6":
            print("Enter matrix size:")
            n, m = map(int, input().split())
            if n != m:
                print("The operation cannot be performed. The matrix must be square.")
                continue
            print("Enter matrix:")
            matrix = [list(map(float, input().split())) for _ in range(n)]
            inverse = inverse_matrix(matrix, n)
            if inverse is not None:
                print("The result is:")
                print_matrix(inverse)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()