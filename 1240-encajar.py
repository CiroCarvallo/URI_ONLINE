cantidad = 0
num = int(input())
while cantidad< num:
    num1,num2 = input().split()
    qtd = 1
    for i in range(len(num2)):
        qtd =qtd* 10
    if int(num1)%qtd == int(num2):
        print("encaixa")
    else:
        print("nao encaixa")
    cantidad += 1
