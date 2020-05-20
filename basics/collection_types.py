# List
int_list = [1, 2, 3]
string_list = ['abc', 'defghi']
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) # Alice
print(names[-1]) # Eric
names[0] = 'Ann' # Lists are mutable

names.append("Sia") # Append to the end
names.insert(1, "Nikki") # Inserts at position 1
names.remove("Bob") # Remove the first occurrence of Bob
names.index("Alice") # Get the index
len(names) # Get the length of the list
names.count('Alice') # Count the occurrence of 'Alice' in the list
names.reverse() # Reverse the order
names[::-1] # Reverse the order
names.pop(3) # Remove and return item at the index

for element in names:
    print (element)

# Tuples - fixed-length and immutable
ip_address = ('10.20.30.40', 8080)
one_member_tuple = ('Only member', )
or_one_member_tuple = 'Only member',
or_or_one_member_tuple = tuple(['Only member'])

# Dictionaries
state_capitals = {
    'São Paulo': 'São Paulo',
    'Minas Gerais': 'Belo Horizonte',
    'Acre': 'Rio Branco',
    'Parana': 'Curitiba'
}
acre_capital = state_capitals['Acre']

for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))

# Set
first_names = {'Adam', 'Beth', 'Charlie'}

my_list = [1,2,3]
my_set = set(my_list)

if 'Adam' in first_names:
    print('Adam')

for element in first_names:
    print (element)

# defaultdict
from collections import defaultdict

state_capitals = defaultdict(lambda: 'São Paulo')
state_capitals['Rio de Janeiro'] = 'Rio de Janeiro'
state_capitals['Acre'] = 'Rio Branco'
state_capitals['Pernambuco'] = 'Recife'
state_capitals['Bahia'] = 'Salvador'

print(state_capitals['São Paulo'])