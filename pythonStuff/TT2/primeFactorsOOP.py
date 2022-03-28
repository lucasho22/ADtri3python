import math

class PrimeFactor:
    def __init__(self):
      # Object of prime factor class will initially have empty list for prime factors and factors
      self.factors = []
      self.prime = []
    def __call__(self, n):
      # Iterate through all possible factors, and add the successful candidates to the list
      for i in range (1, int(math.floor(n/2) + 1)):
        if (n % i == 0):
          self.factors.append(i)
      # Iterate through the factors and check if each one is prime
      for factor in self.factors:
        # Count used for prime testing, set to 0
        count = 0
        for i in range(2, (factor // 2 + 1)):
            if (factor % i == 0):
                # If it does have factors, count is increased by 1
                count = count + 1
                break
        #If count ever changed from 0, then the factor was not a prime number
        #If it didn't, and the number isn't one, then we add it to the prime factors list
        if (count == 0 and factor != 1):
          self.prime.append(factor)
      # If there were no prime factors, meaning the number itself is prime, then we only have none in the list
      if (len(self.prime) == 0):
        self.prime.append("none")
      return self.prime


def tester():
  factors12 = PrimeFactor() 
  print("12's prime factors: " + str(factors12(12))) # Should output 2 and 3
  factors5 = PrimeFactor()
  print("5's prime factors: " + str(factors5(5))) # Should output none