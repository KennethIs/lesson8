print('-' * 65)
print('Morbid Prediction Boye')
print()

print('Description: This program asks you for your current age and tells you the year that you will die (on average).')
print()

x = input('How old are you? ')
x = int(x)
birth = 2018 - x
birth = int(birth)
death = birth + 79

print('...thinking...')
print('...thinking...')
print('...thinking...')
print()

print('You will die in the year...' + str(death))