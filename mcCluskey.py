#!/usr/bin/env python3
# coding=utf-8
# Description: mc Cluskey algorithm 
# feedback: melissa.escobar@utp.edu.co, UTP2019.


#if __name__ ==  __main__ :


class Minterm(object):
    def __init__(self, numDecim, numBinary, numOf1):
        self.numDecim = numDecim
        self.numBinary = numBinary
        self.numOf1 = numOf1

    def getNumDecim(self):
        return self.numDecim

    def getNumBinary(self):
         return self.numBinary
    
    def getNumOf1(self):
        return self.numOf1
    
    def __str__(self):
        return (self.numDecim, self.numBinary, self.numOf1)


#----------------------------------------------

    
  
def convertBinary(dec):
    binary = ''
    while dec // 2 != 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return str(dec) + binary


#function to count the number of ones of a binary number
def contOnes(numBinary):
    contOfOnes = 0
    for i in numBinary:  
        if (i== '1'):
            contOfOnes +=1
    return contOfOnes

# ----------------------------------

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


#Funcion para convertir un numero binario a una expresion logica

def conBinaryToExp(vars, bin):
        
    """funcion que recibe las variables que se utilizaran para asignarlas a cada bit del minterm 
    y recibe tambien el minterm expresado como un numero binario. La funcion convierte el numero binario 
    a la expresion logica que formará parte de la ecuación lógica. 
    NOTA:  Las variables negadas se expresan de la "forma variable *" , por ejemplo a* """


    express = ''
    for i in range(len(bin)):
        if (bin[i] == '0'):
            string = vars[i] + '* ' #si es un cero concateno la letra correspondiente a la posicion
                                     #Con el simbolo elegido parala negacion de la variable 
            express += string

        else:
            string = vars[i] #si es un uno concateno a la cadena auxiliar la letra correspondiente a la posicion
            
            express += string

    return express

#------- funcion recursiva para evaluar por n veces siguientes a la primera vez si se pueden 
# volver a comparar los elementos de la lista

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

                #se agregan los dos elementos que se pueden "mezclar" a la lista
                canMix.append(mix1Minterms[i]) 
                canMix.append(mix1Minterms[j])

                #se agrega el nuevo numero binario modificado a la lista 
                mix2Minterms.append(change)

            else: # si tienen mas de una diferencia, es decir que no se pueden "mezclar"
                noMix.append(mix1Minterms[i])

    #Al terminar las comparaciones, elimino los binarios repetidos en noMix y en canMix

    noMix2 = list(set(noMix))
    canMix2 = list(set(canMix))

    #Evaluo si los elementos de noMix se encuentran en canMix. Si no están, entonces es un primer implicante














 #-----------     main    --------------



def main():
    #Obtener el numero de minterms que se ingresarán:
    numMinterms = int(input("Ingrese por favor el numero de minterms que componen la lista: "))

    #numero máximo de bits requeridos para expresar los numeros de la lista
    numBits = int(input("Ingrese por favor el numero máximo de bits requeridos para expresar los numeros de la lista: "))

    #lista donde se guardarán los valores decimales de los minterms:
    mintermsList = []

    #Lista de minterms convertida a binario
    
    #obtener los minterms de la lista
    print ("Por favor ingrese a continuación los números decimales que componen la lista de minterms:")

    for i in range (numMinterms):
        minDecim = int(input("minterm: "))
        numBinary = ''
        lista =[]
        
        #convertir el numero decimal a binario para agregarlo al objeto y luego a la lista

        n = convertBinary(minDecim)

        #Si el tamaño del numero decimal es menor a la cantidad requerida de bits, se llenará con ceros 

        if (numBits > len(n)):
            numBinary = (numBits - len(n)) * '0' + n
        
        else:
            numBinary = n

        #calcular cuantos unos tiene el binario

        cO = contOnes(numBinary)        

        # Se agrega la cantidad de unos  a la lista auxiliar
        lista.append(cO)

        #print(cO)

        #se crea un objeto de tipo minterm y se envia su decimal, su binario y el numero de 1s que tiene el binario
        objMinterm = Minterm(minDecim, numBinary, cO )

        mintermsList.append(objMinterm)

        #for e in mintermsList:
            #print(e.__str__())



#Ahora se ordenará la lista según la cantidad de unos

        
    listaOrdenada = sorted(mintermsList, key = lambda object : object.numOf1 )

    for e in listaOrdenada:
        print(e.__str__())
    

    #Hace la comparacion inicial para empezar a crear la lista con las comparaciones entre los numeros binarios,
    #lista que despues se iterará nuevamente 

    i=0
    mix1Minterms = [] #lista en donde se guardarán los minterms que tienen solo una diferencia 

    while listaOrdenada[i].numOf1 < listaOrdenada[len(listaOrdenada)-1].numOf1: #mientras la cantidad de 
        # unos de la posicion i sea menor a la máxima cantidad de unos que contiene 
        # la listaOrdenada ordenada, entonces:

        listaAux = []

        for e in range (i+1,  len(listaOrdenada)):
            print( "e is: " + str(e))

            if listaOrdenada[e].numOf1 == listaOrdenada[i].numOf1 +1:
                listaAux.append(listaOrdenada[e])

            else:
                pass

        #A continuacion recorreré cada uno de los elementos de la listaAux comparando sus dígitos
        #con los del minterm que se encuentra en la posicion i. Si solo encuentra una diferencia 
        #entre sus digitos, entonces cambiará el  dítgito diferentepor el caracter '-' y 
        # agregará el minterm a una nueva lista que después será nuevamente 
        #comparada 

        for e in  range (len(listaAux)):
            m = compBinary(listaOrdenada[i].numBinary, listaAux[e].numBinary)
            if m[0] == True: #si solo hay una diferencia entre los numeros binarios
                
                d = cambiarDiferencia(listaOrdenada[i].numBinary, listaAux[e].numBinary, m[1])
                mix1Minterms.append(d) #lo agrega a la lista de minterms con el primer cambio
                #ya no el objeto minterm, si no solamente el numero con el cambio del caracter '-'
            else:
                pass #Si hay más de una diferencia, continua con el siguiente en la listaAux

        
        # --- test  -----    
        print("Para  el "+str(listaOrdenada[i].numOf1) + "la lista es: " )
        for e in listaAux:
            print(e.__str__())
 
        # ---- end of test -----

        i +=1

    print("Primer mix: ")
    for e in mix1Minterms:
        print(e)

    #El siguiente paso es recorrer la lista obtenida para determinar si es posible realizar un
    # nuevo cambio entre sus digitos por el caracter '-'


    primImplicante = [] #lista de los primeros implicantes
    mix2Minterms = []  





main()

