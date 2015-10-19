n = 0
sum = 1
while (n < 23):
  if (n % 5 == 0):
    continue
  else:
    sum = sum + n
  n += 2
print (n)
