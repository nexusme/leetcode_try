test = ["flower", "flow", "flight"]


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ''
    s = strs[0]
    for i in range(1, len(test)):
        while strs[i].find(s) != 0:
            s = s[:-1]
    print(s)
    return s


longestCommonPrefix(test)
