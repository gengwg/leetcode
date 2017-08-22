# -*- coding: utf-8 -*-
"""
75. Sort Colors

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}

        for i in nums:
            count[i] += 1
        # for i in nums:
        #     if i ==0:
        #         count[0]+=1
        #     if i ==1:
        #         count[1]+=1
        #     if i ==2:
        #         count[2]+=2

        nums = []
        for i in range(3):
            nums += [i] * count[i]

        return nums

    def sortColors(self, nums):
        """
        http://www.cnblogs.com/zuoyuan/p/3775832.html
        解题思路：这道题不允许使用排序库函数。
        那么最直观的解法是：遍历两遍数组，第一遍对0，1，2计数，
        第二遍对数组进行赋值，这样是可以ac的。

        但题目的要求是只使用常数空间，而且只能遍历一遍。
        那么思路就比较巧妙了。
        设置两个头尾指针，头指针p0指向的位置是0该放置的位置，
        尾指针p2指向的位置是2该放置的位置。
        i用来遍历整个数组，
        碰到0把它和p0指向的数交换，
        碰到2把它和p2指向的数交换，
        碰到1继续向后遍历。
        有点类似快速排序的分割数组这一步。
        """
        if nums == []:
            return

        p0 = 0;
        p2 = len(nums) - 1;
        i = 0
        while i <= p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                # do not advance i here
                # because p2 position could be 0
                # which can be caught by next condition
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                # advance i here
                i += 1
            else:  # n[i]==1, do nothing
                i += 1

        return nums


if __name__ == '__main__':
    print Solution().sortColors([0, 1, 0, 0, 1, 2, 1, 0])
    print Solution().sortColors([1, 0, 0])