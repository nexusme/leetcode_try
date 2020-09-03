# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

# def getRow(rowIndex):
#     """
#     :type rowIndex: int
#     :rtype: List[int]
#     """
#     rowIndex = rowIndex + 1
#
#     finalnum = []
#     # print('第', rowIndex, '行')
#     n_1 = 1
#     for i in range(1, rowIndex):
#         n_1 *= i
#     # print('n-1累乘', n_1)
#
#     m_1 = 1
#     n_m_1 = 1
#     # m-1的累乘
#     for m in range(1, rowIndex + 1):
#         # print('m', m)
#         if m == 1:
#             m_1 = 1
#             # print('m = ', m, 'm-1累为：', m_1)
#         else:
#             m_1 *= (m - 1)
#             # print('m = ', m, 'm-1累为：', m_1)
#
#         k = rowIndex - m
#         print('k', k)
#         # n-m的累乘
#         if k == 0:
#             n_m_1 = 1
#             # print('n-m累为：', n_m_1)
#         else:
#             for j in range(1, k + 1):
#                 n_m_1 *= j
#             # print('n-m累为：', n_m_1)
#             result = n_1 / n_m_1 / m_1
#             finalnum.append(int(result))
#             # print('result', int(result))
#
#         n_m_1 = 1
#     finalnum.append(1)
#     print(finalnum)
#     return finalnum


def getRow(num):
    temp = 1
    res = []
    for i in range(num + 1):
        res.append(temp)
        temp = temp * (num - i) // (i + 1)

    print(res)


getRow(3)
