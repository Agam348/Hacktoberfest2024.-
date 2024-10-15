# printing original list
print("The original list is : " + str(test_list))
 
# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()
res = []
for idx, sub in enumerate(test_list, start = 0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))
 
print("The converted list : " + str(res))
