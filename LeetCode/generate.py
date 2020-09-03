# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# def generate(numRows):
#     """
#     :type numRows: int
#     :rtype: List[List[int]]
#     """
#     finalnum = []
#     print('第', numRows, '行')
#     n_1 = 1
#     for i in range(1, numRows):
#         n_1 *= i
#     # print('n-1累乘', n_1)
#
#     m_1 = 1
#     n_m_1 = 1
#     # m-1的累乘
#     for m in range(1, numRows + 1):
#         # print('m', m)
#         if m == 1:
#             m_1 = 1
#             # print('m = ', m, 'm-1累为：', m_1)
#         else:
#             m_1 *= (m - 1)
#             # print('m = ', m, 'm-1累为：', m_1)
#
#         k = numRows - m
#         print('k', k)
#         # n-m的累乘
#         if k == 0:
#             n_m_1 = 1
#             print('n-m累为：', n_m_1)
#         else:
#             for j in range(1, k + 1):
#                 n_m_1 *= j
#             print('n-m累为：', n_m_1)
#             result = n_1 / n_m_1 / m_1
#             finalnum.append(int(result))
#             print('result', int(result))
#
#         n_m_1 = 1
#     finalnum.append(1)
#     print(finalnum)
#     return finalnum

def generate(numRows):
    res = []
    for row in range(numRows):
        res.append([])

        for j in range(row + 1):
            if j == 0 or j == row:
                res[row].append(1)
            else:
                res[row].append(res[row - 1][j - 1] + res[row - 1][j])
    return res


generate(5)
