def run():
    
    # dictionary = {"number " : "", "pwdr3": "" }
    # for i in range (1,101):
    #     if i%3 != 0:
    #         dictionary [i] =i
    #         dictionary [i]= i**3

    # for key, value in dictionary.items():
    dict = {i: i**3 for i in range (1,101) if 1%3 !=0}
    print(dict)

    root = {i: round(i**.5) for i in range (1,1001)}
    print(root)

if __name__ == "__main__":
    run()



#dictionary = {"number " : "i for i in range (1,101)", "pwdr3": "c**3 for c in range(1,101)" }