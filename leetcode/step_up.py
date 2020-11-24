# -*- coding: UTF-8 -*-

# һֻ����һ�ο�������1��̨�ף�Ҳ��������2��̨�ס������������һ�� n?����̨���ܹ��ж�����������

# ����Ҫȡģ 1e9+7��1000000007����������ʼ���Ϊ��1000000008���뷵�� 1��

# ʾ�� 1��

# ���룺n = 2
# �����2
# ʾ�� 2��

# ���룺n = 7
# �����21
# ʾ�� 3��

# ���룺n = 0
# �����1
# ��ʾ��

# 0 <= n <= 100
# ע�⣺��������վ 70 ����ͬ��https://leetcode-cn.com/problems/climbing-stairs/

# ��쳲����ƽ����̨�����⣬����ʱ�临�Ӷȣ��Ϳռ临�Ӷȶ������Ϲ���
def f(n):
    if n <= 0:
        return 1
    elif n==1:
        return 1
    else:
        return f(n-1) + f(n-2)
print('fei bo na qie', f(30))


# ��̬�滮
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

print('dong tai gui hua ', Solution().numWays(30))


# �ݹ���䷨
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