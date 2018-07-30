cantidad=0
casos=int(input())
while cantidad<casos:
    lista2=[]
    lista=input()
    for e in lista:
        if (ord(e)>=65 and ord(e)<=90) or (ord(e)>=97 and ord(e)<=122):
            lista2.append(ord(e)+3)
        else:
            lista2.append(ord(e))
    lista2.reverse()
    medio=int(len(lista2)/2)
    for i in range(medio,len(lista2)):
        lista2[i]=lista2[i]-1
    for i in range(len(lista2)):
        lista2[i]=chr(lista2[i])
    lista3=''.join(lista2)
    print(lista3)
  
    cantidad=cantidad+1
