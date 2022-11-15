from re import I


print('1부터 n까지 정수의 합')

n = int(input('n을 입력하세요.'))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수 합은 {sum}')
print(f'i 값은 {i} 입니다.')