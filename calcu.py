import os 
os.system ('clear')
while True:
  print('\n \tp جمع')
  print('\n \tc طرح')
  print('\n \ty قسمة')
  print('\n \tx ضرب')

  calculations = input('\n\nwhats kind of calculation ')
  os.system ("clear")

  if calculations.lower() == 'p':
      a = input ('\nwrite first number: ')
      b = input ('another number: ')
      a = int(a)
      b = int(b)
      p = a + b
      print(int(p))
      enf = input('\n\n\tenough ???  ')
      if enf =="y" or enf =="Y" or enf =="Yes" or enf =="yes" or enf =="yeah" or enf =="Yeah":
          break
      os.system ('clear')      

  elif calculations.lower() == 'c':    
      a = input ('\nwrite first number: ')
      b = input ('another number: ')
      a = int(a)
      b = int(b)
      c = a - b
      print(int(c))
      enf = input('\n\n\tenough ???  ')
      if enf =="y" or enf =="Y" or enf =="Yes" or enf =="yes" or enf =="yeah" or enf =="Yeah":
          break
      os.system ('clear')
  elif calculations.lower() == 'x':
      a = input ('\nwrite first number: ')
      b = input ('another number: ')
      a = int(a)
      b = int(b)
      x = a * b
      print(int(x))
      enf = input('\n\n\tenough ???  ')
      if enf =="y" or enf =="Y" or enf =="Yes" or enf =="yes" or enf =="yeah" or enf =="Yeah":
          break
      os.system ('clear')
  elif calculations.lower() == 'y':
      a = input ('\nwrite first number: ')
      b = input ('another number: ')
      a = int(a)
      b = int(b)
      y = a / b
      print(int(y))
      enf = input('\n\n\tenough ???  ')
      if enf =="y" or enf =="Y" or enf =="Yes" or enf =="yes" or enf =="yeah" or enf =="Yeah":
          break
      os.system ('clear')
  else:
      os.system('clear')
      print('Not Found')