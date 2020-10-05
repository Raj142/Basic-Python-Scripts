# Python program to swap two variables



aa = input('Ente value of a: ')
b = input('Enter value of b: ')


temp = aa
aa = b
b = temp

print('The value of a after swapping: {}'.format(aa))
print('The value of b after swapping: {}'.format(b))