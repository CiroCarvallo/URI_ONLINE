cantidad=0
casos=int(input())
vector=[6,2,5,5,4,5,6,3,7,6]
while cantidad<casos:
    led= input()
    valor = 0
    for i in range(len(led)):
        valor=valor + vector[int(led[i])]
    print(valor, "leds")
    cantidad=cantidad+1
