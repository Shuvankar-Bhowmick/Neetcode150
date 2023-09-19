'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
'''
import collections
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        rows, cols = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0: # Gate found
                    q.append((i, j))
                    visited.add((i, j))
                
                  
        def bfs():
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            dist = 1
            
            while q:
                qLen = len(q)
                for i in range(qLen):    
                    row, col = q.popleft()
                    
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (r in range(rows) and
                            c in range(cols) and
                            (r, c) not in visited and
                            rooms[r][c] != -1
                            ):
                            rooms[r][c] = dist
                            q.append((r, c))
                            visited.add((r, c))
                dist += 1
                            
            
        bfs()
        for room in rooms:
            print(room, "\n")

solution = Solution()    
solution.walls_and_gates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
)            
            
            
                        