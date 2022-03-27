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
  
