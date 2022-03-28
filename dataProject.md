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

### Organization Screenshot

### Factorial Function with Classes

### My own math function: Prime Factors. OOP code

### Prime Factors in Imperative form

## Github Links

## Replit links

