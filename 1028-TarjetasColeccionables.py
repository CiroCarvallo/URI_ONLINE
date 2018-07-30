cantidad=0
casos=int(input())
while cantidad<casos:
    numero1,numero2= map(int,input().split())
    while not numero2==0:
        a=numero2
        numero2=numero1%numero2
        numero1=a
    print(numero1)
    cantidad=cantidad+1
