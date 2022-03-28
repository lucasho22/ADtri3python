import re
import math

class Palindrome: 
  def __init__(self):
    # Intializing result to true; will change if it is not palindrome
    self.result = True
  # object attribute "thing" is what is being tested by the class
  def __call__(self, thing):
    # Again setting self.result to true so that it resets after each call
    self.result = True
    # Converting to string for indexing purposes
    thing = str(thing)
    # Saving original to be displayed later
    original = "\"" + thing + "\""
    # Manipulating thing so that there are no special characters or uppercase letters
    thing = re.sub('\W+','', thing)
    thing = thing.lower()
    # Iterating through the characters checking if the first one matches the last one
    for i in range(0, math.floor(len(thing)/2)):
      if thing[i] != thing[-(i+1)]:
        # If the corresponding characters don't match, then result is set to false
        self.result = False
        break
    # If the loop never set result to false, then it is palindrome
    if self.result == True:
      return (str(original) + " is a palindrome")
      
    if self.result == False:
      return (str(original) + " is not a palindrome")

def tester():
  test = Palindrome() # Instantiating an object of palindrome class
  print(test("A man, a plan, a canal -- Panama!")) # Is palindrome
  print(test("1! heh#heh    !1")) # Is palindrome
  print(test("hello")) # Is not palindrome
  print(test(12321)) # Is palindrome
  print(test(12221)) # Is palindrome
  print(test(12314)) # Is not palindrome

  