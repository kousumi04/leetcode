class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for p, c in prerequisites:
            adj[c].append(p)
        def dfs(c):
            if c not in preMap:
                preMap[c]=set()
                for p in adj[c]:
                    preMap[c] |= dfs(p)
                preMap[c].add(c)    
            return preMap[c]  
        preMap={}
        for c in range(numCourses):
            dfs(c)
        res=[]    
        for u, v in queries:
            res.append(u in preMap[v])
        return res            