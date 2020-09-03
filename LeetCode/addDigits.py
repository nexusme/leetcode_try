# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例:
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    n = str(num)
    while len(n) > 1:
        tmp = 0
        for a in n:
            tmp += int(a)
        tmp = str(tmp)
        n = tmp
    print(n)
    return int(n)


addDigits(38)
