def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="UTF-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)

def write():
    names =["Omar", "pepe", "augusto", "incomodin", "Rocío","Juan"]
    with open("./archivos/names.txt", "w", encoding="UTF-8") as f:
        for element in names:
            f.write(element)
            f.write("\n")


def  run():
    #read()
    write()

if __name__ == "__main__":
    run()