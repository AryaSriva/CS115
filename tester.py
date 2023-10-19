def insertion_sort(lst, length):
    for i in range(1, length):
        current = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = current
        print(lst)

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort(lst, length):
    unsorted = length
    while unsorted > 1:
        s = 0
        for j in range(1, unsorted):
            if lst[j] < lst[j-1]:
                swap(lst, j-1, j)
                s = j
        unsorted = s
        print(lst)

def selection_sort(lst, length):
    for i in range(0, length - 1):
        min_j = i
        for j in range(i+1, length):
            if lst[j] < lst[min_j]:
                min_j = j
        if min_j != i:
            swap(lst, i, min_j)
        print(lst)


insertion_sort([78,15,23,2,97,85], 6)

