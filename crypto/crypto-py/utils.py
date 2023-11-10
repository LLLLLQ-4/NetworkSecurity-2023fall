import numpy as np
def generate_IV():
    pass

def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x

def modulo_inverse(num, modulo):
    num = num % modulo
    gcd, x, _ = extended_euclidean_algorithm(num, modulo)

    if gcd == 1:
        return x % modulo
    else:
        return "non inverse"

def modulo_matrix_inverse(matrix, modulo):
    det = round(np.linalg.det(matrix)) % modulo
    det_inverse = modulo_inverse(det, modulo)
    matrix_inverse = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            sub_matrix = np.delete(matrix, j, axis=0)
            sub_matrix = np.delete(sub_matrix, i, axis=1)
            det_sub = round(np.linalg.det(sub_matrix)) % modulo
            coefficient = -1 if (i+j) % 2 == 1 else 1
            matrix_inverse[i][j] = det_inverse * coefficient * det_sub % modulo
    matrix_inverse = np.array(matrix_inverse)
    return matrix_inverse        