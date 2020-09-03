# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例1:
# 输入: "hello"
# 输出: "holle"

# 示例2:
# 输入: "leetcode"
# 输出: "leotcede"

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    cl = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    L = 0
    R = len(s) - 1
    while L < R:
        if s[L] in cl and s[R] in cl:
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            L += 1
            R -= 1
        elif s[L] in cl and s[R] not in cl:
            R -= 1
        elif s[L] not in cl and s[R] in cl:
            L += 1
        else:
            L = L + 1
            R = R - 1
    print(''.join(s))


reverseVowels("hello")
