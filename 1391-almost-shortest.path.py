from collections import deque
import copy
dist={}
dist2={}
C2 = 0
C1 =0
def Dijktra(G,pesos,s):
    global C1
    for e in pesos.keys():
        C1+= pesos[e]
    for v in G.keys():
        dist[v] = C1
    dist[s] = 0
    Q = dist.copy()
    while Q:
        v = min(Q, key=lambda key: Q[key])
        Q.pop(v, None)
        for z in G[v]:
            if dist[z] > dist[v] + pesos[v, z]:
                Q[z] = dist[v] + pesos[v, z]
                dist[z] = dist[v] + pesos[v, z]
def Dijktra2(G,pesos,s):
    global C2
    for e in pesos.keys():
        C2 = C2 + pesos[e]
    for v in G.keys():
        dist2[v] = C2
    dist2[s] = 0
    Q = dist.copy()
    while Q:
        v = min(Q, key=lambda key: Q[key])
        Q.pop(v)
        for z in G[v]:
            if dist2[z] > dist2[v] + pesos[v, z]:
                Q[z] = dist2[v] + pesos[v, z]
                dist2[z] = dist2[v] + pesos[v, z]


N,M=map(int,input().split())
while not N == 0 and not M == 0 :

    G1 = {}
    G2={}
    pesos1 = {}
    pesos2={}
    for i in range(N):
        G1[i] = []
        G2[i]=[]
    s, d = map(int, input().split())
    for i in range(M):
        u, p, w = map(int, input().split())
        G1[u].append(p)
        G2[p].append(u)
        pesos1[u, p] = w
        pesos2[p,u]=w
    Dijktra(G1,pesos1,s)
    Dijktra2(G2,pesos2,d)
    G3=copy.deepcopy(G1)
    for v in G1:
        for w in G1[v]:
            if dist[v]+pesos1[v,w]+dist2[w]==dist[d]:
                G3[v].remove(w)

    Dijktra(G3,pesos1,s)
    if not dist[d]==C1:
        print(dist[d])
    else:
        res=-1
        print(res)
    dist={}
    dist2={}
    N,M=map(int,input().split())
