import math

try:
  num = int(input("Two digit number: "))
  firstDigit = math.floor(num/10)
  # print(firstDigit)
  secondDigit = num - firstDigit * 10
  # print(secondDigit)
  sp = ' ' * 6 
  ln = '-' * 50
  
  print("0" + str(firstDigit) + sp + "0" + str(secondDigit) + sp + "0" + str(firstDigit) + "+0" + sp +  str(num))

  print(ln)

  for i in range(2, 13):
    if (len(str(firstDigit * i)) < 2):
      print("0" + str(firstDigit * i))
    else:
      print(firstDigit * i)
    if (len(str(secondDigit * i)) < 2):
      print('{:>10} '.format("0" + str(secondDigit * i)))
    else:
      print('{:>10} '.format(str(secondDigit * i)))
    print('{:>20} '.format(str(firstDigit * i) + "+" + str(math.floor(secondDigit * i/10))))
    print('{:>30} '.format(str(firstDigit * i + math.floor(secondDigit * i/10)) + str(math.floor(secondDigit * i - 10 * math.floor(secondDigit * i/10)))))



except:
  print("enter two digit number")