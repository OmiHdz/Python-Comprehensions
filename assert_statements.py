
def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors

    ##Comprehensions
    # i for i in range () if ...
        assert num > 0, "Debes ingresar un número mayor a cero"    
        divisors = [i for i in range (1, num +1) if num % i ==0]
        return divisors
         

def run():
    
    num = input("ingresa un número")
    assert num.isnumeric(),"Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")
   
    #print("Debes ingresar un número")

if __name__ == "__main__":
    run()