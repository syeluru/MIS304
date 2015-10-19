# Program to compute the largest prime factor of a number

def compute_primes(number):
  for num in range(1,number):
    if number % num == 0:
      for num2 in range(1,num):
        if num % num2 == 0:
          print (num)
          
compute_primes(24)
    