import math
dx = 0.01
limit = 10000
start = -limit
end = limit

area = 0
x = start
while x <= end:
    if x != 0:
        area += math.sin(x) / x * dx
    x += dx

print(area)