for i in range(int(input())):
    lista = []
    n = int(input())
    while n != 0:
        m = n % 10
        lista.append(m)
        n//=10
    lenght = len(lista)
    l2 = (lenght//2) +1
    

    if lenght == 1:
        print(lista[0])
    elif (lenght % 2 != 0 and lenght != 1):
        print(lista[lenght//2])
    elif (lenght % 2 == 0 and lenght != 1):
        print("*")