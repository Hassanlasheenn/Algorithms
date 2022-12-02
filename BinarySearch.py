def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 6, 5, 7, 8]

print (binary_search(my_list, 3))
print (binary_search(my_list, -1))

# O notation (Chapter 1)

# if there are list of elements
# the simple search takes n elements to search for the list which is o(n) n is the number of operations.
# while the binary search needs log n elements to check the list of size n O(log n).
# Big O notation doesn't tell the speed in seconds it tells how fast the algorithms grows


# Selection sort (Chapter 2) // arrays and linked lists 


