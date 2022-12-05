# O notation (Chapter 1)

# if there are list of elements
# the simple search takes n elements to search for the list which is o(n) n is the number of operations.
# while the binary search needs log n elements to check the list of size n O(log n).
# Big O notation doesn't tell the speed in seconds it tells how fast the algorithms grows


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


# Selection sort // arrays and linked lists 

# Quick sort is faster sorting algorithm than Selection sort

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))
# 
# arrays allow fast reads 
# linked lists allow fast inserts and deletes



# Recursion =>  a function that calls itself
# many important algorithms use recursions

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key")

# base case and recursive case

# base case is when the function doesn't call itself again.
# recursive case is when the funcction calls itself.

# so this prevent the infinite loop

# countdown function 

def countdown(i):
    print(i)
    if i<=0:
        return  #return nothing / stop
    else:
        countdown(i-1)

        
# Stack #

# when using stack it means that the computer is saving information for many function calls.
# so, two options are there 
# use loops in my code
# use tail recursion but this is an advanced topic and not used by some languages.



# Quick Sort #

# the general technique is divide and conquer and quick sort uses this. 

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1, 2, 3, 4]))


# recursive function example

# we get the base case

# sum [] = 0

# the recursive case

# sum(x:xs) = x + sum(xs)

# recursive funtion to count numbers in list 

def count_rec(lst):
    if not lst:
        return 0
    return 1 + count_rec(lst[1:])

print(count_rec([1, 5, 4, 9]))

    # find the maximum number in a list 

flats = [100, 2, 300, 10, 11, 1000]

largest_num = flats[0]

for number in flats:
    if number > largest_num:
        largest_num = number
print(largest_num)

    # or we can use a max() 

flats = [100, 2, 300, 10, 11, 1000]

max_number = max(flats)

print(max_number)

        
### how to quick sort an array using Divide & Conquer ####
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))


            # Hash Tables # => maps keys to values 

book = dict()   #dictionaries in Python are hash tables
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(book["avocado"])

# build a phone book hash tables 
# use curly braces as a shortcut to dict()
phone_book = {
    "Jenny": 8675309,
    "emergency": 911
}

print(phone_book["Jenny"]);

# create a hash to keep track of people who voted

voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick him out!")
    else:
        voted[name] = True
        print("Let them vote!")


check_voter("Mike")
check_voter("Mike")

        # create a caching #

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data



            ## Breadth-first search ##


