print('세 정수의 중앙값')
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b 

print(f'중앙값: {med3(a, b, c)}')