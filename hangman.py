from os import error, replace, sep
import random
from typing import ValuesView

def read():
    data =[]
    try:
        with open("archivos\data.txt","r",encoding="UTF-8") as f:
            for element in f:
                data.append(element)
    except(TypeError,NameError,SyntaxError,FileNotFoundError):
        print("no podemos encontrar el archivo, dirijase con su programador en turno ")    
    hang(data)

def showData():
    data=[]

    with open("archivos\data.txt","r",encoding="UTF-8") as f:
        for element in f:
            data.append(element)
    for count, element in enumerate(data,start=1):
        print(count,"-", element)
        

#elimina palabras a través de su índice y reescribe el archivo    
def delElement(): 


    showData()
    data=[]

    with open("archivos\data.txt","r",encoding="UTF-8") as f:
        for element in f:
            data.append(element)

    deleteWord =""
    deleteIndex = int(input("Ingrese el indice del elemento a borrar "))
    c=-1
    
    for item in data:
        c= c+1
    try:
        if deleteIndex > c:
            raise ValueError("Indice fuera de los límites, intenta con otro indice menor a: ",c+1)
    except ValueError as ve:
        print(ve)
        return False

    #comparamos el indice a borrar con la cuenta, cuando coinciden igualamos la palabra a borrar con el elemento del indice
    for count, element in enumerate(data, start=1):
            if deleteIndex == count:
                deleteWord=element
                break
    

    #borramos el elemento del indice indicado y posterior a ello recorremos la lista para escribir de nuevo el archivo
    with open("archivos\data.txt","w",encoding="UTF-8") as f:        

        for element in data:
            if deleteWord == element:
                data.pop(deleteIndex-1)
                for element in data:
                    print(element)
                    f.write(element)
    
#Ingresa palabra(s) nuevas a la lista y escribe el archivo
def overWrite():
    try:
        newWords = input("Ingrese la(s) palabra(s) a añadir a la lista separadas por un espacio y presione enter \n")
        newWords = newWords.split(sep=None)
        if not newWords:
            raise ValueError("No puedes dejar el espacio completamente vacío")
        for item in newWords:
            if item.isalpha() == False:
                raise ValueError("Ingresa únicamente palabras, no números ni simbolos, separados por espacios.")    
            
    except ValueError as ve:
        print(ve)
        return False               

    with open("archivos\data.txt","a",encoding="UTF-8") as f:
        for item in newWords:
            f.write("\n")
            f.write(item)
    
            

def hang(data):
    #obtenemos un elemento random de la lista data
    word = random.choice(data)
    #descomponemos la palabra en letras, la enumeramos y
    # guardamos en una nueva lista enumerada
    wordList = list(enumerate(word))
    #borramos el último caracter de la palabra "\n"
    wordList.pop(len(wordList)-1)
    #se crea una lista de la palabra a comparar
    compWord = []
    compWord = list(word)
    compWord.pop(len(compWord)-1)
    



    print("Adivina la palabra: ")

    # for item in wordList:
    #     print (item, end=" "),
    #     #print(" _ ", end= " ")
    
    # print(" ")

    #creamos una lista llamada intento para llenar las 
    #letras de la palabra
    attempt = []
    x=0
    #contamos cuantos elementos tiene la palabra
    for item in compWord:
        x= x+1
    #llenamos de basura _ la longitud de la palabra en el arreglo attempt        
    [attempt.append(" _ ") for element in range (0,x)]
    print(*attempt, sep = "_ ")

    #Evaluamos, mientras el attempt no sea igual a la palabra comparada o se terminen las vidas
    lives = 8
    while attempt != compWord:
        
        print("Vidas restantes", lives-1)
        if lives == 0:
            break
        
        
        letter = input("Ingresa la letra: ")
        
        try:
            if len(letter) ==0:
                raise ValueError("No ingreses caracteres vacíos")
        except ValueError as ve:
            print(ve)
            return False 
        try:
            if len(letter) >1:
                raise ValueError("No ingreses más de un caracter")
        except ValueError as ve:
            print(ve)
            return False            
        
        assert letter.isalpha(), "Ingresa únicamente letras, no  números ni caracteres especiales "
        
        
            
        
       #ciclo para recorrer la palabra a comparar con la letra ingresada
       # y sustituir esa letra en el indice adecuado del attempt
        c= 0      
        for item in compWord:
            
            if letter == item:
                
                attempt.pop(c)
                attempt.insert(c,letter)
                attempt.index(letter)
                print(*attempt, sep = " ")
            c= c+1
        
        if letter in attempt:
            lives = lives
        else:
            lives = lives -1 
        hangman = " "
        if lives == 7:
            print('''
            +---+
            |   |
            |   |
                |
                |
                |
                |
            =========''')
        
        elif lives == 6:
            hangman='''
            +---+
            |   |
            |   |
            O   |
                |
                |
                |
            ========='''
            print(hangman)

        elif lives == 5:
            hangman='''
            +---+
            |   |
            |   |
            O   |
            |   |
                |
                |
                |
            ========='''
            print(hangman)

        elif lives == 4:
            hangman='''
            +---+
            |   |
            |   |
            O   |
            |   |
           /|   |     
                |
                |
            ========='''
            print(hangman)

        elif lives == 3:
            hangman='''
            +---+
            |   |
            |   |
            O   |
            |   |
           /|\  |     
                |
                |
            ========='''
            print(hangman)

        elif lives == 2:
            hangman='''
                +---+
                |   |
                |   |
                O   |
                |   |
               /|\  |     
               /    |
                ========='''
            print(hangman)

        elif lives == 1:
            print('''
  +---+
  |   |
  |   |
  O   |
  |   |
 /|\  |     
 /    |
   
=========''')


    if lives == 0:
                print("Lo siento, no tienes más vidas, intenta nuevamente")              
                print('''
  +---+
  |   |
  |   |
  O   |
  |   |
 /|\  |     
 / \  |
   
=========''')
                print("La palabra correcta era: ", word)
    else:
        print("Felicidades! la palabra correcta es :", word)


def run():
    try:

        option =int(input("Presiona: \n 1 para ver la lista completa de palabras \n 2 para eliminar alguna palabra por su índice \n 3 para añadir una palabra al final de la lista \n 4 para jugar hangman \n"))
        
        if option <1 or option >4:
            raise Exception("Debes ingresar un número entre el 1 y el 4")
        
        if option == 1:
            showData()
        elif option == 2:
            delElement()
        
        elif option == 3:
            overWrite()        
        elif option == 4:
            read()
            
    except ValueError:
        print("Debes ingresar un número")
    except Exception as ve:
                print(ve)
                return False

if __name__ == "__main__":
    run()