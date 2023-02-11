n = int(input())
s = n
sum = 0
while s>0:
  i = s%10
  sum += i**3
  s = s//10
if sum==n:
  print("Armstrong number")
else:
  print("Not an Armstrong number")
