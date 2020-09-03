# 统计所有小于非负整数 n 的质数的数量。
# 示例:
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 暴力
# def countPrimes(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#
#     # 2为最小的质数，从2开始做穷举，直到这个数本身
#     count = 0
#     for i in range(2, n):
#         # 从2到获取到的数求余，余数为0则不是质数，跳出循环
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             # 求余不为0则为质数
#             count += 1
#
#     print(count)

# 厄拉多塞筛法


def countPrimes(n):
    isPrimes = [1] * n
    res = 0
    for i in range(2, n):
        if isPrimes[i] == 1:
            res += 1
        j = i
        while i * j < n:
            isPrimes[i * j] = 0
            j += 1
    return res


countPrimes(10)
