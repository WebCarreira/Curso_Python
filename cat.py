#Given the below class:

class cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

#1- Instantiate the cat object with 3 cats
cat1 = cat('Farrusco', 5)
cat2 = cat('Preto', 2)
cat3 = cat('Melga', 1)

#2- Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args, key=lambda cat: cat.age)

oldest = oldest_cat(cat1, cat2, cat3)

#3- Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest.age} years old.')
print(f'{oldest.name} is the oldest cat.')