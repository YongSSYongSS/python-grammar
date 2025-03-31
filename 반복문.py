"""
2739
N = int(input())

for x in range(9):
    print(N, "*" , x+1 , "=" , N*(x+1))

10950
times = int(input())

for x in range(1,times+1):
    A,B = map(int, input().split())
    print(A+B)


8393
n = int(input())

total = 0

for x in range(1,n+1):
    total += x

print(total)


25304
X = int(input())
N = int(input())

sum = 0

for i in range(1, N+1):
    a, b=map(int, input().split())
    sum += a*b

if X == sum:
    print("Yes")
else :
    print("No")

25314
A = int(input())

byte = A // 4
answer = "int"

for i in range(1, byte+1):
    answer = 'long ' + answer

print(answer)

15552
import sys
T = int(input())

for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)

11021
T = int(input())

for i in range(1,T+1):
    A,B = map(int, input().split())
    print("Case #"+str(i)+":",A+B)


11022
T = int(input())

for i in range(1,T+1):
    A,B = map(int, input().split())
    print("Case #"+str(i)+":",A,"+",B,"=",A+B)


2438
n = int(input())

for i in range(1,n+1):
    print("*"*i)



2439
n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

10952
while 1:
    A,B = map(int, input().split())
    if (A == B== 0):
        break
    else :
        print(A+B)


10951
for i in range(5):
    A , B = map(int, input().split())
    print(A+B)
"""

while 1:
    try :
        A , B = map(int, input().split())
        print(A+B)
    except :
        break