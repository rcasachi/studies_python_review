# Booleans - bool

issubclass(bool, int)
isinstance(True, int)
isinstance(False, int)

logical_and = x and y
logical_or = x or y
logical_not = not x

arithmetic_bool = True + False == 1
arithmetic_bool = True * True == 1

# Numbers
int_value = 100

float_value = 2.0
float_value = 100.e0

complex_value = 2 + 1j
complex_value = 100 + 10j

# Strings
str_value = 'hello'
bytes_value = b'hello'
h_string = str_value[0]
hel_string = str_value[0:3]

# Tuple
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))

print(a + b)
print(a[0])

# List
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'another language'
print(b[0:2])
print(b * 2) # print twice
print(a + b) # concatenate the lists

# Set - Unique values
a = {1, 2, 'a'}
a.add('z')

# Frozensets
# They are immutable and new elements cannot added after its defined.
b = frozenset('kasjdasji')

# Dict - Unique Key-Value pairs
a = {
    1: 'one',
    2: 'two'
}
b = {
    'a': [1, 2, 3],
    'b': 'a string'
}
print(b['a'])
print(a.values())
print(a.keys())