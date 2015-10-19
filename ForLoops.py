'''
print ("what is missing in\n\t\tthe output?")

print (95 // 25) # to get the number of quarters
print (95 % 25)
'''

def main():

  for i in range (0,10):
    print (i, " ", end=' ')
  print('\n')

  for i in range(10):
  	print (i, end=' ')
  print('\n')

  i = 1
  while ( i <= 9):
  	print (i, end = ' hello ')
  	i += 1
  print ()
  print ()

  state = "california"
  for i in state:
  	print (i, end=' ')
  print ()

  i = 0
  while (i < len(state)):
  	print (state[i], end = ' ')
  	i += 1
  print ()

  for i in range (10):
  	print (i, end = ' ')
  	print ("hello")
  print ()

  for letter in "Jurassic World":
  	print ("Current letter:", letter)
  


main()