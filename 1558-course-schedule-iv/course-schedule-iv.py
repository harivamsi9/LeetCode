class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # initializing pre-req relationship matrix
        isPrereq = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        # set the prereq relationships
        for pre in prerequisites:
            a, b = pre
            isPrereq[a][b] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPrereq[i][k] and isPrereq[k][j]:
                        isPrereq[i][j] = True

        result = []
        for query in queries:
            u, v = query
            result.append(isPrereq[u][v])
        return result
        


        