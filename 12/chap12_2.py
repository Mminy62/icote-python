n = sorted(input())
temp = 0
result = ''

for s in n:
    if s.isdecimal():
        temp += int(s)
    else:
        result += s

if temp == 0 and str(temp) in n:
    temp = 0

print(result+str(temp))