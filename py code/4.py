a=input("please enter time:")
H = int(a[0:2])
M = int(a[3:5])
S = int(a[6:8])
time = H*3600 + M*60 + S
print(time)
