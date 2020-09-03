# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#

# 输出: "100"

# 思路1： 转回十进制 再转回二进制
# 思路2：补齐使之等长 相加 进位

test_a = "111"
test_b = "1"


def addBinary(a, b):
    # a = int(a, 2)
    # b = int(b, 2)

    print(bin(int(a, 2) + int(b, 2))[2:])
    return bin(int(a, 2) + int(b, 2))[2:]


addBinary(test_a, test_b)
