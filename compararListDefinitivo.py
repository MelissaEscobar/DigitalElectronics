

lista = [0,1,1,1,1,3,4,4,4,4,4,5,6,6]

i=0
while lista[i] < lista[len(lista)-1]: #mientras la cantidad de unos de la posicioni sea menor a 
    #la máxima cantidad de unos que contiene la lista ordenada, entonces:

    listaAux = []

    for e in range (i+1,  len(lista)):
        print( "e is: " + str(e))

        if lista[e] == lista[i] +1:
            listaAux.append(lista[e])

        else:
            pass

    #test     
    print("Para  el "+str(lista[i]) + "la lista es: " + str(listaAux))

    i +=1
