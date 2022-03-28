class Factorial:
  def __init__(self):
      # Intially have 1 since in factorial you multiply by 1 at the end
      self.facNum = 1
  def __call__(self, n):
    if n < self.facNum:
      return self.facNum
    else:
      # At first, it is n * self(n-1)
      # Then, self(n-1) calls the function again, and it will have value (n-1) * self(n-2)
      # This keeps going until the n-1 argument in self is less than 1, which will then then return 1 for self(0)
      # The result is n * (n-1) * (n-2) * (n-3) ... * 1 which is factorial
      facAnswer = n * self(n-1) 
    return facAnswer

def tester():
  # Create instance of factorial object
  fac_of = Factorial() 
  try: 
    x = int(input("What is the number you want to take factorial of? "))
    print(fac_of(x)) 
  except:
    print("Enter an integer")

