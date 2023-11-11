x = float(input())
y = float(input())
sum = 0
for i in range(x, y + 1):
    if i % 5 == 0:
        sum = sum + i
print(sum)