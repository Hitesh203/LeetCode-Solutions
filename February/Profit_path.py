#2467. Most Profitable Path in a Tree Feb-24/2025
from collections import deque
class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        n = len(edges) + 1
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent =[-1] * n
        depth = [0] * n
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v] and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    visited[v] = True
                    q.append(v)
        
        bob_dict ={}
        current = bob
        time = 0 
        while current != -1:
            bob_dict[current] = time
            current = parent[current]
            time += 1
        children_count = [0] * n
        for u in range(n):
            if u == 0:
                children_count[u] =len(adj[u])
            else:
                children_count[u] = len(adj[u]) -1
        max_profit = -float('inf')
        
        if 0 in bob_dict:
            t_alice = depth[0]
            t_bob = bob_dict[0]
            if t_alice < t_bob:
                initial = amount[0]
            elif t_alice == t_bob:
                initial = amount[0] // 2
            else:
                initial = 0
        else:
            initial = amount[0]
        stack = [(0, initial)]
        while stack:
            u, current_sum = stack.pop()
            if children_count[u] == 0:
                if current_sum > max_profit:
                    max_profit = current_sum
            else:
                for v in adj[u]:
                    if v!= parent[u]:
                        if v in bob_dict:
                            t_alice_v= depth[v]
                            t_bob_v = bob_dict[v]
                            if t_alice_v < t_bob_v:
                                add_val = amount[v]
                            elif t_alice_v == t_bob_v:
                                add_val = amount[v] // 2
                            else:
                                add_val = 0
                        else:
                            add_val = amount[v]
                        stack.append((v,current_sum + add_val))
        return max_profit