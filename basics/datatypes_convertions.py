a = '123'
b = int(a)

a = '123.456'
b = float(a)
c = int(b)

a = 'hello'
b = list(a) # ['h','e','l','l','o']
c = set(a) # {'o','e','l','h'}
d = tuple(a) # ('h','e','l','l','o')

# Explicit string type definition of literals
bytes_string = b'foo bar'
str_string = u'foo bar'
raw_string = r'foo bar'
