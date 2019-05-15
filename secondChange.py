
#Comparar dos cadenas de numeros binarios, revisa donde esta la diferencia
def compBinary(s1,s2):
    count = 0
    pos = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
            pos = i
    if count == 1:
        return True, pos
    else:
        return False, None

#---------------------------
#Funcion para cambiar la diferencia entre dos cadenas de numeros binarios por el caracter '-'
def cambiarDiferencia(s1, s2, diff): #diff es la posicion donde esta la dferencia
        
    arrayS1 = []
    #Agrego cada char del string a una lista, para hacer el cambio respectivo segun el  indice
    #en el que cambian las dos cadenas
    for i in s1:
        arrayS1.append(i)
    #Se hace el cambio del caracter por '-'
    arrayS1[diff] = '-'
    #lo  regreso nuevamente como una cadena
    str1 = ''.join(str(e) for e in arrayS1)
 
    return str1

def mixAgain(mix1Minterms): #recibe la lista de numeros binarios y los caracteres '-'
    #y devuelve una lista con los primeros implicantes, los numeros binarios nuevamente modificados  
    # y un booleano que dice si se pudo efectuar un cambio 
    
    noMix = [] #lista de los minterms que podrían ser primeros implicantes
    canMix = [] #lista de los minterms que se pueden mezclar nuevamente

    #Estas son las dos listas que retorna la funcion
    primImplicante = [] #lista en donde se agregaran los que son definitivamente primeros implicantes
    mix2Minterms = [] #lista en donde se agragaran los numeros binarios con el nueo cambio

    for i in range (len(mix1Minterms)):

        for j in range (i+1, len(mix1Minterms)):
            comp = compBinary(mix1Minterms[i], mix1Minterms[j])

            if comp[0]== True: # si las cadenas tienen solo una diferencia, nuevamente se hará el cambio por '-'
                change = cambiarDiferencia(mix1Minterms[i], mix1Minterms[j], comp[1] )
                print("el " + str(mix1Minterms[i]) + " se mezcla con " + str(mix1Minterms[j]) + " Y produce: ")
                print(change)

                #se agregan los dos elementos que se pueden "mezclar" a la lista
                canMix.append(mix1Minterms[i]) 
                canMix.append(mix1Minterms[j])

                #se agrega el nuevo numero binario modificado a la lista 
                mix2Minterms.append(change)
                print("Lista minterms actualizada : ")
                print(mix2Minterms)

            else: # si tienen mas de una diferencia, es decir que no se pueden "mezclar"
                noMix.append(mix1Minterms[i])

    #Al terminar las comparaciones, elimino los binarios repetidos en noMix y en canMix

    noMix2 = list(set(noMix))
    canMix2 = list(set(canMix))

    #Evaluo si los elementos de noMix se encuentran en canMix. Si no están, entonces es un primer implicante

    for e in noMix2:
        if e in canMix2: #Si el elemento de noMix2 se encuentra en canMix2
            pass #porque quiere decir que el elemento no es primer implicante
        
        else:
            primImplicante.append(e)

    if canMix2:#si la lista no esta vacia, retorna la lista de primeros implicantes, canMix2 y True
        return (primImplicante, mix2Minterms,  True)

    else:
        return( primImplicante, mix2Minterms, False )

# test
l = ['0101-', '00-10', '10-00', '0000-', '00-10']

print ( mixAgain(l))