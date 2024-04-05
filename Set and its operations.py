# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Printing sets
print("Set 1:", set1)
print("Set 2:", set2)

# Adding elements to a set
set1.add(6)
print("Set 1 after adding element 6:", set1)

# Removing elements from a set
set2.remove(8)
print("Set 2 after removing element 8:", set2)

# Set union
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# Set intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Set difference
difference_set = set1.difference(set2)
print("Difference between Set 1 and Set 2:", difference_set)

# Set symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference between Set 1 and Set 2:", symmetric_difference_set)

# Checking for subset
subset_check = {4, 5}.issubset(set1)
print("Is {4, 5} a subset of Set 1:", subset_check)

# Checking for superset
superset_check = set1.issuperset({1, 2})
print("Is Set 1 a superset of {1, 2}:", superset_check)
