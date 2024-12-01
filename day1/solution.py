import numpy as np

list1, list2 = np.array([]), np.array([])

with open("input.txt") as f:
    for line in f:
        items = line.split("   ")
        list1 = np.append(list1, int(items[0]))
        list2 = np.append(list2, int(items[1]))

list1 = np.sort(list1)
list2 = np.sort(list2)

diff = np.absolute(list2 - list1)
summation = np.sum(diff)

print(list1[:5])
print(list2[:5])
print(diff[:5])
print(summation)

# print(len(list1))
# print(len(list2))