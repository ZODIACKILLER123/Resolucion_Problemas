for i in range(int(input())):
    l, a, b = map(int, input().split())
    lista = list(map(int, input().split()))
    suma = []
    c = 0
    for i in range(len(lista)):
        if i >= a and i <= b:
            suma.append(lista[i])
    print(sum(suma))