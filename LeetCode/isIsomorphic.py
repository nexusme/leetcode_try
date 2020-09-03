# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true
test = "egg"
test2 = "add"

# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false

# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true

test3 = "ab"
test4 = "ca"


#  暴力法
# def isIsomorphic(t, s):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     save = []
#     save2 = []
#     for i in range(0, len(t) - 1):
#         for j in range(1, len(t)):
#             if t[i] == t[j] and i != j:
#                 save.append(i)
#                 save2.append(j)
#
#     pattern = save + save2
#
#     save3 = []
#     save4 = []
#     for i in range(0, len(s) - 1):
#         for j in range(1, len(s)):
#             if s[i] == s[j] and i != j:
#                 save3.append(i)
#                 save4.append(j)
#
#     pattern2 = save3 + save4
#
#     print(pattern)
#     print(pattern2)
#
#     print(pattern == pattern2)
#     return pattern == pattern2


def isIsomorphic(t, s):
    dic = {}
    tmp = []
    for i in range(0, len(t)):
        dic[t[i]] = i
    for i in dic:
        tmp.append(dic[i])

    dic2 = {}
    tmp2 = []
    for i in range(0, len(s)):
        dic2[s[i]] = i
    for i in dic2:
        tmp2.append(dic2[i])
    print(tmp)
    print(tmp2)
    print(tmp == tmp2)
    return tmp == tmp2


isIsomorphic(test3, test4)
