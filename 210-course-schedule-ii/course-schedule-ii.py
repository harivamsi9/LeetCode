class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        if prerequisites == []: 
            return [x for x in range(numCourses)]

        # build graph
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            if a not in graph:
                graph[a] = []


        # find the indegree of the graph
        def find_indegree(graph):
            indegree = {node:0 for node in graph}
            for node in graph:
                for neigh in graph[node]:
                    if neigh in indegree:
                        indegree[neigh] += 1

            return indegree

        def find_topo(graph):
            ans = []
            indegree = find_indegree(graph)
            queue = []

            for node in indegree:
                if indegree[node] == 0:
                    queue.append(node)

            while queue:
                node = queue.pop(0)
                ans.append(node)
                for neigh in graph[node]:
                    if neigh in indegree:
                        indegree[neigh] -= 1
                        if indegree[neigh] == 0:
                            queue.append(neigh)

            return ans if len(ans) == len(graph) else []

        ans = find_topo(graph)
        if ans:
            if len(ans) < numCourses:
                set_ = set(ans)
                for i in range(numCourses):
                    if i not in set_:
                        ans.insert(0,i)

        return ans








                