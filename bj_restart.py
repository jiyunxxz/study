# t = int(input())
# iii=[]
# for i in range(0,t,1):
#     a,b = map(int,input().split())
#     iii.append(a+b)
# for n in iii:
#     print(n)

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# a = int(input())
# b = int(input())
# sum = 0
# for i in range(b):
#     c,d = map(int,input().split())
#     sum += c*d
# if sum == a:
#     print("Yes")
# else:
#     print("No") #25304번 영수증

# a = int(input())
# print("long "*(a//4)+"int") #사실체육이었다어쩌고

# import sys

# a = int(sys.stdin.readline())
# for i in range(a):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a+b) #15552

# import sys

# a = int(sys.stdin.readline())
# d = 1

# for i in range(a):
#     b,c = map(int,sys.stdin.readline().split())
#     print(f"Case #{d}: {b + c}")
#     d += 1  # 11021

# a = int(input())
# for i in range(a):
#     b,c = map(int,input().split())
#     print("Case #%d: %d + %d = %d"%(i+1,b,c,b+c))  #다음거 

# a= int(input())
# for i in range(a):
#     print(str("*"*(i+1)).rjust(a)) !!!!! 2439번 반드시 다시 풀어볼것.

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except EOFError:
#         break  #반복문 마지막문제


# a = int(input())
# sum= 0
# d = list(map(int,input().split()))
# # for i in range(a):
# #     b.append(random.randint(1,100))
# c = int(input())
# for i in d:
#     if i == c:
#         sum += 1
# print(sum)   #1차원 배열 첫번째 문제

# a,b = map(int,input().split())
# c = list(map(int,input().split()))
# d =[]
# for i in c:
#     if i < b:
#         d.append(i)
# print(*d) #### print(*리스트명)을 하면, 리스트의 요소들을 공백을 두고 자동 출력해준다. ####

# 여기까지내가 짠 코드고 

# n,x=map(int,input().split())
# l=list(input().split())

# for i in range(n):
#     if int(l[i]) < x : 리스트에서 하나씩 꺼내서 정수형으로  만들어준다.
#         print(l[i],end=" ") 그 값을 출력하는데, 공백을 두고 출력한다.
#  #다른분이짠 코드

a = int(input())
b = list(map(int,input().split()))
d = []
max = max(b)
min = min(b)
d.append(min)
d.append(max)
print(*d)  #10818 