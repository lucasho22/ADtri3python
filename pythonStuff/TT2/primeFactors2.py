import math

def primeFactors(num):
  # Empty lists that will store factors and prime factors
  factors = []
  primeFactors = []
  # This loop generates all factors of the number
  for i in range (1, int(math.floor(num/2) + 1)):
    if (num % i == 0):
      factors.append(i)
  # From the determined factors, this code will check which are prime
  # First loop iterates through all the factors
  for factor in factors:
    # Count used for prime testing, set to 0
    count = 0
    # This loop is used to check if the factor itself has any factors
    for i in range(2, (factor // 2 + 1)):
        if (factor % i == 0):
            # If it does have factors, count is increased by 1
            count = count + 1
            break
    #If count ever changed from 0, then the factor was not a prime number
    #If it didn't, and the number isn't one, then we add it to the prime factors list
    if (count == 0 and factor != 1):
      primeFactors.append(factor)
  # If there were no prime factors, meaning the number itself is prime, then we only have none in the list
  if (len(primeFactors) == 0):
    primeFactors.append("none")
  return primeFactors


def tester():
  print("12's prime factors: " + str(primeFactors(12))) # Should output 2 and 3
  print("5's prime factors: " + str(primeFactors(5))) # Should output none


