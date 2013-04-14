#The elements in a set are nonduplicates and are not placed in any particular order

set1 = {"green", "red", "blue", "red"}
print(set1)

set2 = set([7,1,2,23,2,4,5])
print(set2)

set3 = set1 | {"green", "yellow"} #Union
print(set3)

set3 = set1 - {"green", "yellow"} # difference
print(set3)

set3 = set1 & {"green", "yellow"} # intersection
print(set3)

set3 = set1 ^ {"green", "yellow"} # exclusive or
print(set3)
