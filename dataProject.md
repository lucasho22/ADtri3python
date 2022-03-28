{% include navigation.html %}

# Data Structures Project

### Replit embed below. May need to change the run function in .replit.

{% include replit.html %}

# Week 0

## Code snippets

### Code for pattern animation:

```python 
def pattern_print(position):
    print(ANSI_HOME_CURSOR)
    print(CANDLE_COLOR)
    sp = " " * position
    print(FIRE_COLOR)
    print(sp + "    (   ")
    print(sp + "    )\   ")
    print(sp + "    {_}   ")
    print(CANDLE_COLOR, end="")
    print(sp + "   .-;-.   ")
    print(sp + "  |'-=-'| ")
    print(sp + "  |     | ")
    print(sp + "  |     | ")
    print(sp + "  |     | ")
    print(sp + "  '.___.' ")

# Pattern function, iterface into this file
def patternfunc():

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate candle moving
    for position in range(start, distance, step):
        pattern_print(position)  # call to function with parameter
        time.sleep(.1)
```

### Code for Keypad

```python
def format(matrix):
    rows = len(matrix)
    for x in range(rows):
        columns = len(matrix[x])
        for i in range(columns):
            print(matrix[x][i], end=' ')
        print()

def format_tester():
    matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
    format(matrix)
    matrix2 = [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ]
    format(matrix2)
```

### Code for Swap

```python
def swap(a, b):
    arranged_lst = []
    lst = [a, b]
    while len(lst) > 0:
        smallest = min(lst)
        arranged_lst.append(smallest)
        lst.remove(smallest)
    return arranged_lst[0], arranged_lst[1]
```

### Key Code for menu and submenu

```python
main_menu = [
    ["keypad", keypad.format_tester],
    ["swap", swap.test_swap]
]

patterns_sub_menu = [
    ["pattern", pattern.patternfunc]
]

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["pattern", patterns_submenu])
    buildMenu(title, menu_list)


def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            os.system('clear')
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  # recursion, start menu over again

if __name__ == "__main__":
    menu()
```

### Code for Tree

```python
def createTree(height):
  i = 1
  while(i<=height):
    starInRow = "* " * i
    n = 3 * height - i
    sp = " " * n
    print(sp + starInRow + "\n")
    i = i + 1
  print(" " * 3 * (height-1) + "* * *\n" + " " * 3 * (height-1) + "* * *")
```

## Github Links

[Issue for menu, submenu, and swap and keypad functions](https://github.com/AD1616/ADtri3python/issues/1)

[Issue for pattern animation](https://github.com/AD1616/ADtri3python/issues/2)

[Issue for tree pattern](https://github.com/AD1616/ADtri3python/issues/3)

## Replit links

[Link to menu which contains runtime of this week's progress](https://replit.com/@AD1616/ADtri3python#pythonStuff/menu.py)

# Week 1

## Code snippets

### Code for InfoDB lists

```python
# Hack 1
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "StudentFirstName": "Sahil",  
               "StudentLastName": "Samar",  
               "Classes":["AP Physics","AP Calc BC","AP English Language","AP US History", "AP CSP"]  
              })  

InfoDb.append({  
               "StudentFirstName": "Anirudh",  
               "StudentLastName": "Ramachandran",  
               "Classes":["AP Chemistry","AP Stats","AP CSP","AP Gov", "AP CSP", "Expos"] 
              })  

InfoDb.append({  
               "StudentFirstName": "Michael",  
               "StudentLastName": "Chen",  
               "Classes":["Civics/Econ","AP Stats","AP CSP","AP Physics", "World lit"] 
              })  

InfoDb.append({  
               "StudentFirstName": "Ethan",  
               "StudentLastName": "Vo",  
               "Classes":["AP Bio","AP Stats","AP CSP","AP Gov", "Expos"] 
              })
```

### Code for print data function and loops

```python
# Hack 2
def print_data(n):
    print(InfoDb[n]["StudentFirstName"], InfoDb[n]["StudentLastName"])  # using comma puts space between values
    print("\t", "Classes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes"]))  # join allows printing a string list with separator
    print()
  
def for_loop():
    # calls print data function for n and iterates until all elements in list are covered
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    # calls print data function iteratively until it reaches the last element in list
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    # Calls itself until the if condition is not met
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```

### Code for fibonacci function and tester

```python
# Hack 3

def fib(n):
  # Top two conditions there so that when 0 and 1 are reached, fib(n-1) + fib(n-2) can be computed
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return fib(n-1) + fib(n-2) #This adds up the two numbers of the sequence before n

def fibTester():
  # Input for number of terms for fibonacci sequence 
  num = int(input("Enter a number for fibonacci: "))

  # Try/except used in case user types in a negative number or a non-number character
  try: 
    i = 0
    sequence = []
    # While loop used to call the fib function for all values until and including the user input; this generates the entire sequence
    while (i <= num):
      sequence.append(fib(i))
      i +=1
    print("The sequence is", end = ' ')
    # For loop is there so that the entire sequence is printed without the brackets
    for i in range(num):
      print(sequence[i+1], end = ', ')

    # Prints out the final fib number separately if user is just looking to find the last fib number
    print("and the number", num , "fibonnaci number is", fib(num))
  except:
    print("...Sorry, please type in a positive integer.")
```

## Github Links

- [Issue for InfoDB lists and loops](https://github.com/AD1616/ADtri3python/issues/5)
- [Issue for Fibonacci](https://github.com/AD1616/ADtri3python/issues/6)

## Replit links

- Runtime from menu
- [Link to code for hacks](https://replit.com/@AD1616/ADtri3python#pythonStuff/TT1/hacks.py)

# Week 2

## Snippets

### Organization Screenshots

![image](https://user-images.githubusercontent.com/64157584/160328272-edb68876-9e89-4bbe-9b07-f11c1a0a77ff.png)

![image](https://user-images.githubusercontent.com/64157584/160328319-b1b7a6ef-b527-4e42-9cc2-81073350e923.png)

![image](https://user-images.githubusercontent.com/64157584/160328365-0a8a2d0f-1c5b-4ff2-91a5-061565428893.png)


### Factorial Function with Classes


```python
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
```


### My own math function: Prime Factors. OOP code


```python
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
```


### Prime Factors in Imperative form


```python
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
```


### Palindrome Code


```python
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
```


## Github Links


[Factorial Issue](https://github.com/AD1616/ADtri3python/issues/10)

[Own Math Function Issue](https://github.com/AD1616/ADtri3python/issues/11)

[Palindrome Issue](https://github.com/AD1616/ADtri3python/issues/12)


## Replit links

[Updated Menu](https://replit.com/@AD1616/ADtri3python#pythonStuff/menu.py)
