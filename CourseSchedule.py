"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from ast import List


def canFinish(self, numCourses: int, prerequisites) -> bool:
    # need a visit set to keep track of the nodes visited
    visit = set()
    crsMap = {i: [] for i in range(numCourses)}

    # Fill the hashmap
    for crs, pre in prerequisites:
        crsMap[crs].append(pre)

    # Dfs algorithm
    def dfs(crs):
        if crs in visit:
            return False
        if crsMap[crs] == []:
            return True

        visit.add(crs)
        for pre in crsMap[crs]:
            if not dfs(pre):
                return False

        visit.remove(crs)
        crsMap[crs] = []
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True
