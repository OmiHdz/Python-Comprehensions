import math

def run():
    # square = []
    # for i in range(1,101):
    #     if i%3 !=0:
    #         square.append(i**2)

    square = [i**2 for i in range(1,101) if i % 3 !=0]
    print (square)

    mcm =[i for i in range (1,100000) if i %36 ==0]
    print(mcm)

if __name__ == "__main__":
    run()
