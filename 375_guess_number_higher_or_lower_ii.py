# 375. Guess Number Higher or Lower II

# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
#
# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
#
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.


class Solution(object):
    # https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, L, R):
        if L >= R:
            return 0
        if dp[L][R]:
            return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R+1))
        return dp[L][R]

    # https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84769/Two-Python-solutions
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi]) for x in range(lo, hi))
        return need[1][n]


print(Solution().getMoneyAmount(10))

