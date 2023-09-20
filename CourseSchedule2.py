'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # For this question we will be doing a dfs solution
        ans = []
        visited, cycle = set(), set()

        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True

            if adj[crs] == []:
                ans.append(crs)
                visited.add(crs)
                return True
            
            visited.add(crs)
            cycle.add(crs)
            for dep in adj[crs]:
                if not dfs(dep): return False
            cycle.remove(crs)

            adj[crs] = []   # Signifies that the specific course is not dependent on any other courses any longer
            ans.append(crs)
            return True 
        
        for i in range(numCourses):
            if not dfs(i): return []

        return ans               
     
        
        