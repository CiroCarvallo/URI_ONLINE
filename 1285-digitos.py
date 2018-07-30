from sys import stdin

for dato in stdin:
    num1,num2=map(int,dato.split())

    contador=0

    for i in range(num1,num2+1):
        lista=str(i)
        conjunto=set()
        seRepite=False
        for e in lista:
            if e in conjunto:
                seRepite=True
            else:
                conjunto.add(e)
        if not seRepite:
            contador+=1
    print(contador)
