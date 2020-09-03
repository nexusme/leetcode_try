#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
# 假设我们的环境只能存储得下 32 位的有符号整数，
# 则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。

m = 123


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    thisInt = list(str(x))
    # 符号判断
    if x < 0:
        thisInt.remove('-')
        thisInt.reverse()
        # 合并字符串
        r = -int(''.join(thisInt))
    else:
        thisInt.reverse()
        r = ''.join(thisInt)
        r = int(r)

    if not -pow(2, 31) <= r <= pow(2, 31) - 1:
        r = 0

    # list(map(int, x.split()))
    print(r)
    return r


reverse(m)
