from os import remove

name = ' Sergey '
print(f'Hello {name}, would you like to learn some Python today?')
print(f'Hello {name.upper()}, would you like to learn some Python today?')
print(f'Hello {name.lower()}, would you like to learn some Python today?')
print(f'Hello {name}, would you like to learn some Python today?'.title())
print('\tAlbert Einstein once said, "A person who never made\n\ta mistake never tried anything new."')
famous_person = name
messag = 'Einstein once said, "A person who never made\n\ta mistake never tried anything new."'
print(f'\t{famous_person} {messag}')
print(name)
print(f'\t {name.lstrip()} \n')
print(f'\t {name.rstrip()} \n')
print(f'\t {name.strip()} \n')