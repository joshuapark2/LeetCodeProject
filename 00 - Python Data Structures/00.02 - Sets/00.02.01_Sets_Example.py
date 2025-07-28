# Removes duplicates from the dictionary using curly braces {}
basket = {'apple', 'oranges', 'pineapple', 'oranges'}
print(basket)
print('oranges' in basket) # True
print('blue berries' in basket) # False

# Creating an empty set using the set() function
a = set('abracadabra')
b = set('alacazam')
print(a) # Unique letters in a
print(b) # Removes all duplicates but gives a different print statement b/c unordered collection

print(a - b, 'letters in a but not b')
print(a | b, 'letters in a or b or both')
print(a & b, 'letters in both a and b')
print(a ^ b, 'letters in a or b but not both')