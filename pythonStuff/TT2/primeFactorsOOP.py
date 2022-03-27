import math

class PrimeFactor:
    def __init__(self):
      self.num = []
      self.prime = []
    def __call__(self, n):
      for i in range (1, int(math.floor(n/2) + 1)):
        if (n % i == 0):
          self.num.append(i)
      for factor in self.num:
        count = 0
        for i in range(2, (factor // 2 + 1)):
            if (factor % i == 0):
                count = count + 1
                break
        if (count == 0 and factor != 1):
          self.prime.append(factor)
      return self.prime


findPrimeFactors = PrimeFactor() 
x = int(input("What is the number you want to find factors of? "))
print(findPrimeFactors(x)) 


