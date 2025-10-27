# Time - O(V + E), Space - O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {i: [] for i in range(numCourses)}
        for p, c in prerequisites:
            preReqs[c].append(p)
        
        visiting = set()

        def dfs(curr: int) -> bool:
            if curr in visiting:
                return False
            if preReqs[curr] == []:
                return True

            visiting.add(curr)

            for pre in preReqs[curr]:
                if not dfs(pre):
                    return False
            
            visiting.remove(curr)
            preReqs[curr] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True