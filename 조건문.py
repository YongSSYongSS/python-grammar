"""

1330
A, B = map(int, input().split())

if A>B:
    print("<")
elif A<B:
    print(">")
else:
    print("==")


9498
score = int(input())
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else :
    print("F")

2753

---- 내 답----
A = int(input())

if ((A%4)==0) and ((A%100)!=0):
    print("1")
elif ((A%100)==0) and ((A%400)!=0):
    print("0")
elif (A%400)==0:
    print("1")

    
---- 인터넷 ----
year = int(input())

if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')


14681
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else :
    print("4")

2884
h,m = map(int, input().split())


if 45 <= m <=59:
    print(h, m-45)
elif h!=0 and (0 <= m <= 44):
    print(h-1, 60-(45-m))
elif h==0 and (0 <= m <= 44):
    print(23, 60-(45-m))


h,m = map(int, input().split())
term = int(input())

a = m + term

if (a//60) > (term//60) :
    if h == 23 :
        h == 0
        a == a % 60
        print (h, a)
    else :
        h += (a//60) 
        b = a % 60
        print (h, b)


print(h, a)



H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60    #시간은 동작시간의 60을 나눈 몫을 더한다
M += timer % 60     #분은 동작시간의 60의 나머짓값을 더한다

if M >= 60:         #그럼에도 분이 60을 넘을 경우
    H += 1          #시에 1 추가
    M -= 60         # 60 빼기기
if H >= 24:
    H -= 24

print(H,M)


a, b, c= map(int, input().split())

if a == b == c:
    print(10000 + 1000*a)
elif a==b and a!=c:           #elif (a==b and a!=c):   는 왜 안되죠...?
    print(1000 + 100*a)
elif b==c and b!=a:
    print(1000 + 100*b)
elif c==b and c!=a:
    print(1000 + 100*c)
elif a != b!= c:
    if a > b and a > c:
        print(a*100)
    elif b > c and b > a:
        print(b*100)
    else :
        print(c*100)

"""