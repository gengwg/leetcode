# 207. Course Schedule
#
#  There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites,
# for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take.
# To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges,
# not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes)
# on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        http://bookshadow.com/weblog/2015/05/07/leetcode-course-schedule/

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        degrees = [0] * numCourses
        childs = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in childs[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)
        return len(courses) == 0


if __name__ == '__main__':
    print Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print Solution().canFinish(2, [[1,0],[0,1]])
