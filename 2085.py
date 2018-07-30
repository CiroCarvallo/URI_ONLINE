from collections import deque
from collections import defaultdict
def resultado(V,cantAristas,G):
    cantCaminos=defaultdict(lambda :0)
    res=defaultdict(lambda:0)
    res[N]=1
    cantCaminos[N]=1
    for v in V[1:]:
        cantCaminos[v]=sum([cantCaminos[w]*cantAristas[w,v] for w in G[v]])
        res[v]=max([cantCaminos[v] + res[w] for w in G[v]],default=0)
    return res[1]
while True:
    try:
        N, M = map(int, input().split())
        G = {}
        V=set()
        cantAristas = defaultdict(lambda: 0)
        G=defaultdict(lambda:set())
        for i in range(M):
            u, p = map(int, input().split())
            cantAristas[p,u]+=1
            if u not in V:
                V.add(u)
            if p not in V:
                V.add(p)
            if u not in G[p]:
                G[u].add(p)
        V=list(V)
        for v in G:
            G[v]=list(G[v])
        V.sort(reverse=True)
        res=resultado(V,cantAristas,G)
        print(res)
    except EOFError:
        break
