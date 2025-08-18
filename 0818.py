# t = int(input())  

# for i in range(t):
#     s = input()
#     print(s[0] + s[-1])   #9086


# s = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# result = []

# for ch in alphabet:
#     if ch in s:              
#         result.append(s.index(ch))  # 가장 처음 나온 ch의 값이 몇개인지 알려준다. 
#     else:
#         result.append(-1)   

# print(*result)  10809번

# a = input()

# cr = ['dz=','c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in cr:  #cr을 반복해서 a에 있으면 그 부분을 1로 대체한다. 그러면 길이의 수가 줄어들어 총 글자의 수를 알 수 있음.
#     a = a.replace(i,"1")

# print(len(a))   #2941번 

a = int(input())

count = 0
for i in range(a):
    b = list[input()]