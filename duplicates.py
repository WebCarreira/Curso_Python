#Exercise: check for duplicates in list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for values in some_list:
    if some_list.count(values)>1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)