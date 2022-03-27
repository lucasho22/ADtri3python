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

# Hack 2

def for_loop1():
  # def classesDisplay(list):
  #   for x in list:
  #     print(x)
      
  for i in range(len(InfoDb)):
    print(str(InfoDb[i]["StudentFirstName"]) + " First Period Class: " + InfoDb[i]["Classes"][0])


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

      
  
  
  
  