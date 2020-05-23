me = {'name': 'Anna', 'age': 26, 'occupation': ['student', 'employee']}
#print(me)

del me['occupation']
#print(me)

me['occupation'] = ['student', 'employee']
me['interests'] = 'Netflix'



print(me.items())


for key, value in me.items():
    print(key, value)
