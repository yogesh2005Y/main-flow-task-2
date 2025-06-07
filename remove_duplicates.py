def remove_duplicates(lst):
    seen = set()
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
            seen.add(item)
    return unique

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("List without duplicates:", remove_duplicates(lst))


