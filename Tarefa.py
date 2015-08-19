#Problema dos minimos quadrados
#dado inteiro nao negativo n, retornar menor cadeia
#de quadrados cuja soma seja n

def quad(x):
    if x<=1:
        return 1
    elif x < 4:
            lista=[]
            n=0
            for n in range(x):
                lista.append(1)
            return (lista)
    else:
            i=0
            i = x / 4
            d=0
            d = x / i
            lista=[]
            n=0
            for n in range(int(i)):
                lista.append(int(d))
            return (lista)
