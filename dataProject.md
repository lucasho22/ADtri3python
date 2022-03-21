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
InfoDb = []
InfoDb.append({  
               "StudentFirstName": "Sahil",  
               "StudentLastName": "Samar",  
               "Classes":["AP Physics","AP Calc BC","AP English Language","AP US History", "AP CSP"]  
              })  
```

### Code for print data function and loops

```python
def print_data(n):
    print(InfoDb[n]["StudentFirstName"], InfoDb[n]["StudentLastName"])  # using comma puts space between values
    print("\t", "Classes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes"]))  # join allows printing a string list with separator
    print()
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
```

### Code for fibonacci function and tester

```python
def fib(n):
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return fib(n-1) + fib(n-2)

def fibTester():
  num = int(input("Enter a number for fibonnaci: "))
  try: 
    i = 0
    sequence = []
    while (i <= num):
      sequence.append(fib(i))
      i +=1
    print("The sequence is", end = ' ')
    for i in range(num):
      print(sequence[i+1], end = ', ')
    print("and the number", num , "fibonnaci number is", fib(num))
  except:
    print("...Sorry, please type in a positive integer.")
```

## Github Links

[Issue for InfoDB lists and loops](https://github.com/AD1616/ADtri3python/issues/5)
[Issue for Fibonacci](https://github.com/AD1616/ADtri3python/issues/6)

## Replit links

- Runtime from menu
- [Link to code for hacks](https://replit.com/@AD1616/ADtri3python#pythonStuff/TT1/hacks.py)

# Week 3

## Code snippets

## Github Links

## Replit links

