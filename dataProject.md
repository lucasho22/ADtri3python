{% include navigation.html %}

# Data Structures Project

# Week 1

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


def test_swap():
    age1 = int(input("Enter first age: "))
    age2 = int(input("Enter second age: "))
    x, y = swap(age1, age2)
    print(x, y)
```

### Code for menu and submenu

```python
import os
import keypad
import swap
import pattern

main_menu = [
    ["keypad", keypad.format_tester],
    ["swap", swap.test_swap]
]

patterns_sub_menu = [
    ["pattern", pattern.patternfunc]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

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

## Github Links

[Issue for menu, submenu, and swap and keypad functions](https://github.com/AD1616/ADtri3python/issues/1)

## Replit links

# Week 2

## Code snippets

## Github Links

## Replit links


# Week 3

## Code snippets

## Github Links

## Replit links

