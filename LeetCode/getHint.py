# 你写出一个秘密数字，并请朋友猜这个数字是多少。
# 朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
# 朋友根据提示继续猜，直到猜出秘密数字。
# 请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。
#
# xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
# yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
# 请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
#
#  
#
# 示例 1:
# 输入:
secret1 = "1807"
guess1 = "7810"

# 输出: "1A3B"
# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。

# 示例 2:
# 输入:
secret2 = "1123"
guess2 = "0111"

# 输出: "1A1B"
# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
#  
import collections


def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    bull = sum(s == g for s, g in zip(secret, guess))
    cow = len(list((collections.Counter(list(secret)) & collections.Counter(list(guess))).elements())) - bull
    return str(bull) + 'A' + str(cow) + 'B'

    # return "{A}A{B}B".format(A=bull, B=cow)
    # secret_pos = [[secret[i], i] for i in range(len(secret))]
    # guess_pos = [[guess[i], i] for i in range(len(guess))]
    # bull = 0
    # for i in range(len(secret)):
    #     bull += 1 if secret_pos[i][0] == guess_pos[i][0] and secret_pos[i][1] == secret_pos[i][1] else 0
    # print(str(bull) + 'A' + str(cow - bull) + 'B')
    # return str(bull) + 'A' + str(cow - bull) + 'B'


getHint(secret2, guess2)
