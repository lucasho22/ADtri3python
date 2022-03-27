def createTree(height):
  i = 1
  while(i<=height):
    starInRow = "* " * i
    n = 3 * height - i
    sp = " " * n
    print(sp + starInRow + "\n")
    i = i + 1
  print(" " * 3 * (height-1) + "* * *\n" + " " * 3 * (height-1) + "* * *")
    
def createTreeTester():
  height = int(input("Enter how tall you want the tree to be: "))
  createTree(height)
