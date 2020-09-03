# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

test = 0


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    try_num = 0
    # if x <= 0:
    #     print(0)
    #     return 0
    while try_num <= x:
        if try_num * try_num == x or try_num * try_num < x < (try_num + 1) * (try_num + 1):
            print(try_num)
            return try_num

        else:
            try_num += 1


mySqrt(test)
