def my_name(name):
    print ('my name is ' +name)
firstname = 'jana'
my_name(firstname)

def my_meal(food,drink):
    print (f'i like to eat {food} and drink {drink}')

my_meal('mashed potato','pepsi')

def cube (number):
    return number**3
def by_three(number):
    
    if number%3==0:
        return cube(number)
    else:
        return False
print(by_three(7))
