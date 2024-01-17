groceryList = ['apple ', 'cheese ', 'orange ', 'beef ', 'cucumber ']
groceryList = groceryList + [ 'bread ', 'cheese ', 'yogurt ', 'butter ', 'chicken ']
groceryList = groceryList + [ 'beef ', 'beef ', 'chicken ', 'rice ', 'pasta ']

noItems = 0
noMeat = 0
counter = 0

while noItems < len(groceryList):
  if groceryList[noItems] == 'beef ':
    noMeat += 1
  elif groceryList[noItems] == 'chicken ':
    noMeat += 1
  noItems += 1

print("There are", noItems, "items in the grocery list, ")
print(noMeat, "of them must be picked up from the butcher.")