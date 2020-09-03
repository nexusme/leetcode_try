# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
# 示例 2:
#
# 输入: 5
# 输出: false

def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    while num:
        if num == 1:
            return True
        if num % 4:
            return False
        num = num // 4


isPowerOfFour(5)
