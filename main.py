
def ewklid(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n

a = int(input("Введите первое делимое: "))
b = int(input("Введите второе делимое: "))

print("Наибольший общий делитель равен = ",ewklid(a, b))
