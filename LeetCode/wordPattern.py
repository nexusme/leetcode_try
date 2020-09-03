# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
# 输入:
pattern0 = "abba"
str0 = "dog cat cat dog"

# 输出: true

# 示例 2:
# 输入:
pattern1 = "abba"
str1 = "dog cat cat fish"

# 输出: false

# 示例 3:
# 输入:
pattern2 = "aaaa"
str2 = "dog cat cat dog"
# 输出: false

# 示例 4:
# 输入:
pattern3 = "abba"
str3 = "dog dog dog dog"
# 输出: false

pattern4 = "abc"
str4 = "b c a"


# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    


def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    # pattern_list = list(pattern)
    # print('pattern_list', pattern_list)
    # str_to_list = list(filter(None, str.split(" ")))
    # print('str_to_list', str_to_list)
    # distinct_list = list(set(str_to_list))
    #
    # dic = {}
    # compare = []
    # for i in range(len(distinct_list)):
    #     dic[distinct_list[i]] = i
    # print('dic', dic)
    # for name in str_to_list:
    #     if name in dic:
    #         compare.append(dic[name])
    # print("compare", compare)
    # distinct_pattern = sorted(list(set(pattern_list)))
    # distinct_compare = list(set(compare))
    # print("distinct_pattern", distinct_pattern)
    # print("distinct_compare", distinct_compare)
    # com_dict = dict(zip(distinct_pattern, distinct_compare))
    # print("com_dict", com_dict)
    res = str.split()
    # index函数检索 如果包含子字符串返回开始的索引值
    # map计算每一个元素
    print(list(map(pattern.index, pattern)))
    print(list(map(res.index, res)))

    print(list(map(pattern.index, pattern)) == list(map(res.index, res)))


wordPattern(pattern0, str0)
