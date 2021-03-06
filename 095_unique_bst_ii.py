# -*- coding: utf-8 -*-
"""
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


http://www.cnblogs.com/zuoyuan/p/3752428.html

题意：
接上一题，这题要求返回的是所有符合条件的二叉查找树，
而上一题要求的是符合条件的二叉查找树的棵数，
我们上一题提过，
求个数一般思路是动态规划，而枚举的话，我们就考虑dfs了。
dfs(start, end)函数返回以start，start+1，...，end为根的二叉查找树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :param n: int
        :return: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]

        res = []
        for rootval in range(start, end + 1):
            ltree = self.dfs(start, rootval - 1)
            rtree = self.dfs(rootval + 1, end)
            for left in ltree:
                for right in rtree:
                    root = TreeNode(rootval)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


if __name__ == '__main__':
    print Solution().generateTrees(3)
