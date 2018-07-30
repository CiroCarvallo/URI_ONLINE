import heapq
from collections import defaultdict
N, M = map(int, input().split())
while not N == 0 and not M == 0:
    grafo = defaultdict(list) #usa prim y devuelve el peso del arbol generador minimo
    lista=[]
    conjunto = set()
    peso = 0
    for i in range(M):
        a, b, p = map(int,input().split())
        grafo[a].append((p, b))
        grafo[b].append((p, a))

    a = min(grafo.keys())
    conjunto.add(a)
    for b,w in grafo[a]:
        heapq.heappush(lista,(b,w))
    while len(lista)>0:
        p, b = heapq.heappop(lista)
        if b not in conjunto:
            peso += p
            conjunto.add(b)
            for b2,p in grafo[b]:
                heapq.heappush(lista, (b2,p))



    print(peso)
    N, M = map(int, input().split())
