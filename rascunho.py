#def power(x,n):
#    if n==0:
#        return 1
#    else:
#        return x*power(x,n-1)
#print(power(2,3))

#x = 10
#y = 4
# z = x // y #dá erro porque tem espaçamento a mais
#print(z)

car = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}


#print(car.update({'year': 2020}))
#car['year'] = 2020
#car.update({'color' : 'red'}) # ou car['color] = 'red
car.pop('model')
print(car)