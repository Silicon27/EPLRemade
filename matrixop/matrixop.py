from typing import List


def wd_matrix_mul(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """
    2 x 2 matrix multiplication (2 dimensional matrix)
    :param m1:
    :param m2:
    :return:
    """

    # x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0])
    # y1 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0])
    # x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1])
    # y2 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])
    #
    #
    #
    # result.append([x1, x2])
    # result.append([y1, y2])

    # Perform 2x2 matrix multiplication using a loop

    return [
        [sum(m1[i][k] * m2[k][j] for k in range(2)) for j in range(2)] for i in range(2)
    ]


def td_matrix_mul(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """
    3 x 3 matrix multiplication (3 dimensional matrix)
    :param m1:
    :param m2:
    :param m3:
    :return:
    """

    return [
        [sum(m1[i][k] * m2[k][j] for k in range(3)) for j in range(3)] for i in range(3)
    ]


def display_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)


# 2d example matrices
example_2dmatrix1 = [[1, -4], [3, 5]]

example_2dmatrix2 = [[-27, 3], [9, 8]]

# 3d example matrices
example_3dmatrix1 = [[1, -4, 7], [3, 5, 9], [2, 6, 8]]

example_3dmatrix2 = [[-27, 3, 5], [9, 8, 2], [4, 1, 0]]

display_matrix(wd_matrix_mul(example_2dmatrix1, example_2dmatrix2))
print("\n")
display_matrix(td_matrix_mul(example_3dmatrix1, example_3dmatrix2))
