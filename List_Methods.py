basket = ["banana", "Apples", "Oranges", "Blueberries"]

print(basket)

#Remove the "banana"
#basket.pop(0)
basket.remove("banana")
print(basket)

#Remove"Blueberries"
basket.pop(2)
print(basket)

#Put "Kiwi" at the end of the list
basket.append("Kiwi")
print(basket)

#Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
print(basket)

#Count how many apples in the basket
print(basket.count("Apples"))

#Empty the list
print(basket.clear())