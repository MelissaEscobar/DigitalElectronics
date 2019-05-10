def conBinaryToExp(vars, bin):
    express = ''
    for i in range(len(bin)):
        if (bin[i] == '0'):
            string = vars[i] + '* ' #si es un cero concateno la letra correspondiente a la posicion
                                     #Con el simbolo elegido parala negacion de la variable 
            express += string

        else:
            string = vars[i] #si es un uno concatenoa ala cadena auxiliar la letra correspondiente a la posicion
            
            express += string

    return express

print (conBinaryToExp('abcd', '0111'))
