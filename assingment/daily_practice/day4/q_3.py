def overlapping(list,list2):
    result = []
    for item in list:
        if item in list2:
            return True
    return False
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
print(overlapping(list1, list2))  # Output: True