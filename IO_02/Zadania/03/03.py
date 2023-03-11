import math

def count():
    f = open("Zadania/03/in.txt")
    data = f.read().splitlines()
    f.close

    f = open("Zadania/03/out.txt", mode = 'w')
    liczby = []
    for i in range(len(data)):
        liczby.append(int(data[i]))
        f.write(data[i] + " ")
        f.write(str(math.sin(liczby[i])) + "\n")
         
    f.close
count()