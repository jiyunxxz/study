a = int(input())
b = int(input())

b1  = b%10
b2 = (b//10)%10 #십의 자리를 구하는 법 .
b3 = b//100

print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)

#한줄씩 써내려가야하므로 일의자리,십의자리, 백의자리를 구해서 작성하여야한다.