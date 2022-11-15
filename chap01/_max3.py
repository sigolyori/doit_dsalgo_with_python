print('세 정수의 최댓값은?')

a = int(input('정수 a의 값?'))
b = int(input('정수 b의 값?'))
c = int(input('정수 c의 값?'))

def max3(a, b, c):
    '''a, b, c의 최댓값을 구하여 반환'''
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c

    return maximum # 최댓값 반환