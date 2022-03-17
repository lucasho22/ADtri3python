def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence from index 1 to j-1, the term right before A[j]
        i = j-1
        # While loop is checking each term before A[j] to see if it is greater or smaller than A[j]
        while i > -1 and A[i] > key:
            print("i =" + str(i), "j =" + str(j), "key = " + str(key), "A[i] =" + str(A[i]))
            A[i+1] = A[i]
            i = i-1
            print("A = " + str(A))
        A[i+1] = key
        print("A = " + str(A))
    return A

def insertion_sort_tester():
    matrix = [3, 2, 4, 5, 9, 7, 1]
    insertion_sort(matrix)