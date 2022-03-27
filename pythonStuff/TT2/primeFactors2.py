import math

def primeFactors(num):
  factors = []
  primeFactors = []
  for i in range (1, int(math.floor(num/2) + 1)):
    if (num % i == 0):
      factors.append(i)
  for factor in factors:
    count = 0
    for i in range(2, (factor // 2 + 1)):
        if (factor % i == 0):
            count = count + 1
            break
    if (count == 0 and factor != 1):
      primeFactors.append(factor)
  if (len(primeFactors) == 0):
    primeFactors.append("none")
  return primeFactors


def tester():
  print("12 factors: " + str(primeFactors(12))) # Should output 2 and 3
  print("5 factors: " + primeFactors(5)) # Should output none

tester()

