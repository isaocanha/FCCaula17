#fatorial
num = int(input())
res = 1
while num < 0:
    num = int(input())
for i in range (1, num +1):
    res *= i
print(f'{num}!= {res}')
