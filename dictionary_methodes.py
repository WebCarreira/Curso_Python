#1- Create a user profile for your new game
#This user profile will be stored in a dictionary with keys:
# 'age'
# 'username'
# 'weapons'
# 'is_active'
# 'clan'
#2- Iterate and print all the keys in the above user
#3- Add a new weapon to your user
#4- Add a new key to include 'is_banned'. Set it to False
#5- Ban the user by setting the previous key to True
#6- Create a new user2 my copying the previous user and update the age value and username value.

user = {
    'age' : 20,
    'username' : 'Drake',
    'weapons' : ['gun', 'shotgun', 'knife'],
    'is_active' : True,
    'clan' : 'Kingdom'
}

print(user.keys())

user['weapons'].append('sniper')
print(user)

user.update({'is_banned' : False})
print(user)

user.update({'is_banned' : True})
#user['is_banned'] = True
print(user)

user2 = user.copy()
user2.update({'age' : 35, 'username' : 'Rui'})
print(user2)