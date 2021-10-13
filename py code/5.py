a=int(input("please enter second:"))
H = a//3600
x = a/3600 - a//3600
M = int(x*60)
y = x*60 - M
S = int(y * 60) + 1

print(H,":",M,":",S)


