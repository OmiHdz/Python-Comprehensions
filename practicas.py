def max():
    num1 = int(input("Ingrese el primer número a comparar"))
    num2 = int(input("Ingrese un segundo número"))
    if num1 > num2:
        print("El numero mayor es ", num1)
    else:
        print("El número mayor es ", num2)
def max_of_three():
    num1 = int(input("Ingrese el primer número a comparar"))
    num2 = int(input("Ingrese el segundo número a comparar"))
    num3 = int(input("Ingrese el tercer número a comparar"))
    max = 0

    if num1>num2:
        max = num1
        if num1>num3:
            max = num1
        else:
            max =num3
    elif num2>num3:
        max =num2
    else:
         max = num3
    print(max)
    
def long():
    i=0
    chain = input("Ingresa una cadena de texto ")
    for char in chain:
        i= i+1
    print(i)
    
def sum_mult():
    suma =0
    mult =1
    list=[1,2,3,4]
    for item in list:
        suma = suma + item
    print(suma)
    for item in list:
        mult = mult * item
    print(mult)
def inverse():
    chain =input("Ingrese una cadena de texto a invertir ")
    
    print(chain[::-1])

def superposition():
    list = [1,2,"a",5,"c"]
    list1 = [6,"b",2,"c"]

    for item in list:
        for item1 in list1:
            if item == item1:
                print("true")

def histograma():
    list=[1,2,5]
    for item in list:
        print("*" * item)

if  __name__== "__main__":
    histograma()