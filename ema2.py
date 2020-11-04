def MostrarMayor(lista):
    mayor=""
    lengo=0
    for i in range (0,len(lista)):

        if lengo==0:
            lengo=len(lista[i])
            mayor=lista[i]

        elif lengo<len(lista[i]):
            mayor=lista[i]


    print(mayor)