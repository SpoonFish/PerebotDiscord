import math
level = 50
for i in range(50):
    level = i
    print(math.ceil((level**(1.8+level/26.7) + level*40 - 7)-450*(level/21)) +30)