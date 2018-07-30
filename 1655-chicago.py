import math
import heapq
from decimal import Decimal

def dijkstra(adj, costs, s, t):
    ''' Return predecessors and min distance if there exists a shortest path 
        from s to t; Otherwise, return None '''
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
        #print Q
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            #print 'visit:', u
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

L=input().split()
while not len(L)==1:
    N,M=map(int,L)
    G={}
    Lista=[]
    Costos={}
    for i in range(N):
        G[i+1]=[]
    P={}
    for i in range(M):
        a,b,p=map(int,input().split())
        G[a].append(b)
        G[b].append(a)
        Lista.append(-math.log(p*0.01))
        Costos[a,b]=-math.log(p*0.01)
        Costos[b,a]=-math.log(p*0.01)
    path,d=dijkstra(G, Costos, 1, N)
    if not path==None:
        p=math.exp(-d)*100
        res=Decimal(p)
        print(round(res,6),"percent")
    L=input().split()
