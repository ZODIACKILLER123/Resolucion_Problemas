def factorial(n):
    num = 1
    for i in range(1, n+1):
        num = num * i
    return num

def lista(y):
    lista = []
    while y != 0:
        num = y % 10
        lista.append(num)
        y//=10
    return lista


for i in range(int(input())):
    x = int(input())
    lista_pr = lista(x)
    sum = 0
    for ele in lista_pr:
        sum = sum + factorial(ele)
    if sum == x:
        print("Y")
    else:
        print("N")