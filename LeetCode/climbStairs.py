# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        print(n)
        return n
    more_before_n = 0
    before_n = 1
    for i in range(n):
        result = more_before_n + before_n
        more_before_n = before_n
        before_n = result
    print(result)
    return result


climbStairs(6)
