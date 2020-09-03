# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。

# 示例 2:
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.


# def trailingZeroes(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     result = 1
#     count = 0
#     for i in range(1, n + 1):
#         result = result * i
#
#     tmp = str(result)
#
#     for i in reversed(range(len(tmp))):
#         if tmp[i] == '0':
#             count += 1
#         else:
#             print(count)
#             return count


def trailingZeroes(n):
    p = 0
    while n >= 5:
        n = n // 5
        p += n
    print(p)
    return p


trailingZeroes()
