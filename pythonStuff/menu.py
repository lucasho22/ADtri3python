# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import os
from TT0 import keypad
from TT0 import swap
from TT0 import pattern
from TT0 import Tree
from TT1 import hacks

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu

adventure_sub_menu = [["pattern1", pattern.patternfunc], ["Tree", Tree.createTreeTester]]
data_sub_menu = [["Lists and Loops", hacks.tester]]
math_sub_menu = [["Fibonacci", hacks.fibTester], ["swap", swap.test_swap], ["keypad", keypad.format_tester]]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["adventure", adventure_submenu])
    menu_list.append(["data", data_submenu])
    menu_list.append(["math", math_submenu])
    buildMenu(title, menu_list)


def adventure_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, adventure_sub_menu)

def data_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, data_sub_menu)

def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_sub_menu)


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
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
