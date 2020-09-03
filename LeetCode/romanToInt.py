#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 2 写做 II ，即为两个并列的 1。
# 12 写做 XII ，即为 X + II 。
# 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。
# 但也存在特例，例如 4 是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。
# 同样地，数字 9 表示为 IX。
# 这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
str_test = 'MCMXCIV'


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    str_list = list(s)

    # 建立字典形成对应关系
    roma_dict = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'N': 0}
    # 插入自定义字母防止数组长度不够
    str_list += 'N'
    str_list += 'N'

    print(str_list)
    sum = 0
    # 循环
    for i in range(0, len(str_list) - 2):
        # 利用字典对应关系 前一位大于等于后一位时 则为加
        if roma_dict.get(str_list[i]) >= roma_dict.get(str_list[i + 1]):
            sum += roma_dict.get(str_list[i])
        else:
            # 反之为减
            sum -= roma_dict.get(str_list[i])
        # 加上未判断的最后一位
        sum += roma_dict.get(str_list[len(str_list) - 1])
    print(sum)
    return sum


romanToInt(str_test)
