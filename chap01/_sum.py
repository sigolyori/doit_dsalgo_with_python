print('a부터 b까지의 정수 합')
a = int(input('a:'))
b = int(input('b:'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1, 1):
    sum += i

print(f'{a}부터 {b}까지의 합:  {sum}')