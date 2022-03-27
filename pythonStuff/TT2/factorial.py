class Factorial:
    def __init__(self):
        self.facNum = [1]
    def __call__(self, n):
        if n < len(self.facNum):
            return self.facNum[n]
        else:
            facAnswer = n * self(n-1) 
            self.facNum.append(facAnswer) 
        return self.facNum[n]

fac_of = Factorial() 
try: 
  x = int(input("What is the number you want to take factorial of? "))
  print(fac_of(x)) 
except:
  print("Enter an integer")

