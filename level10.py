# 개미수열

s='1' #수열의 시작이 1
for i in range(30) :
    x = s[0] 
    count = 1
    s_dev = ""
    for j in range(1, len(s)) :
        if s[j] != x :
            s_dev += str(count) + str(x)
            x = s[j]
            count = 1
        else :
            count += 1
    s = s_dev + str(count) + str(x)
print(len(s))

# ans = 5808