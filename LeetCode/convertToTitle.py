#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 例如，
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    while n:
        n, y = divmod(n, 26)
        print(n, y)
        if y == 0:
            n -= 1
            y = 26
        res = chr(y + 64) + res
    print(res)
    return res


convertToTitle(703)
