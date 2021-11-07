
def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors

    ##Comprehensions
    # i for i in range () if ...
    try:
        if num <=0:
            raise ValueError("Ingresa un número positivo mayor a 0")
        divisors = [i for i in range (1, num +1) if num % i ==0]
        return divisors
    except ValueError as ve:
       print(ve)
       return False
       
    
        
    

def run():
    try:
        num = int(input("ingresa un número"))
    
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")

if __name__ == "__main__":
    run()