# -*- coding: UTF-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n?级的台阶总共有多少种跳法。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：

# 输入：n = 2
# 输出：2
# 示例 2：

# 输入：n = 7
# 输出：21
# 示例 3：

# 输入：n = 0
# 输出：1
# 提示：

# 0 <= n <= 100
# 注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/

# 用斐波那锲解决跳台阶问题，但是时间复杂度，和空间复杂度都不符合规则
def f(n):
    if n <= 0:
        return 1
    elif n==1:
        return 1
    else:
        return f(n-1) + f(n-2)
print('fei bo na qie', f(30))


# 动态规划
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

print('dong tai gui hua ', Solution().numWays(30))


# 递归记忆法
class Solution(object):
    memo = dict()
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo.keys():
            return self.memo[n]
        elif n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            self.memo[n] = self.numWays(n-1) + self.numWays(n-2)
            return self.memo[n] % 1000000007
        
print('di gui ji yi fa ', Solution().numWays(30))