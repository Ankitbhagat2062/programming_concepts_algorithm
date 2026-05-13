# 1. Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.append
# items= [3,5,7,9,11,13]
# print(items)
# item = items.pop(4)
# print(items)
# items.insert(2,item)
# print(items)
# items.append(item)
# print(items)

# Given_set 
# first_set={ 23, 42, 65, 57, 78, 83, 29}
# second_set={57, 83, 29, 67, 73, 43, 48}
# Write a program to identify their intersection. Remove these common elements specifically from the first_set
# if first_set.intersection(second_set):
#     print("Common elements existed in the first set.")
#     first_set.difference_update(second_set)
#     print("First set after removing common elements using difference_update:", first_set)
# else:
#     print("No common elements existed in the first set.")

# simple method to find intersection and remove common elements from first_set
# intersection = first_set & second_set
# first_set -= intersection
# print("Intersection:", intersection)
# print("First set after removing common elements:", first_set)

# Q3. Write a program to determine if first_set is a subset or superset of second_set. if a relationship
# is found, delete all elements from the set that is identified as the subset.
first_set_3={27, 43, 34}
second_set_3={34, 93, 22, 27, 43, 53, 48}
is_subset = first_set_3.issubset(second_set_3)
is_superset = first_set_3.issuperset(second_set_3)
if is_subset and is_superset:
    print("First set is both a subset and a superset of the second set.")
    first_set_3.clear()
    print("First set after clearing:", first_set_3)
elif is_subset:
    print("First set is a subset of the second set.")
    first_set_3.clear()
    print("First set after clearing:", first_set_3)
elif is_superset:
    print("First set is a superset of the second set.")
    first_set_3.clear()
    print("First set after clearing:", first_set_3)
