# [Do it! 실습 1-8] 1부터 n까지의 합 구하기 2(for 문)

print('1부터 n까지의 합')

n = int(input('n을 입력:'))

sum = 0

for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지의 합은 {sum}')