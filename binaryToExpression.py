def conBinaryToExp(vars, bin):
    express = ''
    for i in range(len(bin)):
        if (bin[i] == '0'):
            string = vars[i] + '* ' #si es un cero concateno la letra correspondiente a la posicion
                                     #Con el simbolo elegido parala negacion de la variable 
            express += string

        elif (bin[i] == '1'):
            string = vars[i] #si es un uno concateno a la cadena auxiliar la letra correspondiente a la posicion
            
            express += string
        else: #En caso de que sea '-' no concatena nada
            pass

    return express

print (conBinaryToExp('abcd', '01-0'))
