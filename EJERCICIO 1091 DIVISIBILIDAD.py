while(True):
    try:
        a, b = map(int, input().split())
        if a % b == 0:
            print(f"{a} es divisible por {b}")
        elif b % a == 0:
            print(f"{b} es divisible por {a}")
        else:
            print(-1) 
    except EOFError:
        break