def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Sorted list:", bubble_sort(lst))