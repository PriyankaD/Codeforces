n,k = map(int,input().split())
factors = []
for i in range(1, n + 1):
       if n % i == 0:
           factors.append(i)
import random
#print(factors)
random.seed(58)
r = random.choice(factors)
m = r
