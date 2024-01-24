
x="its string not sting > asting haha"

mr ="X"
# Concatenate
print('Hey! ' + x + ' and I am ' + x)

# String Formatting

# Arguments by position
print('Hey! {x} and I am {mr}'.format(x=x, mr=mr))

# F-Strings (3.6+) | in js is string literals
print(f'Hey! {x} and I am {mr}')

print(x.capitalize() )
print(x.upper() )
print(len(x))


# Replace
print(x.replace('world', 'everyone'))

# Count
sub = 'h'
print(x.count(sub))

# Starts with
print(x.startswith('hello'))

# Ends with
print(x.endswith('d'))

# Split into a list
print(x.split())

# Find position
print(x.find('r'))

# Is all alphanumeric
print(x.isalnum())

# Is all alphabetic
print(x.isalpha())

# Is all numeric
print(x.isnumeric())
