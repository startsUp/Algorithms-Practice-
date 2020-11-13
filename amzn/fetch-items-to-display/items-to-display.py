def getItemsToDisplay(numOfItems, items, sortParam, sortOrd, itemsPerPage, pageNum):
    itemsArr = []
    for k in items.keys():
        itemsArr.append((k, items[k][0], items[k][1]))
    itemsArr.sort(key=lambda x: x[sortParam], reverse=True if sortOrd == 1 else False)
    return itemsArr[itemsPerPage * pageNum: itemsPerPage * pageNum + itemsPerPage]

items = {'item1': (10,15), 'item2': (3,4), 'item3': (17,8)}
print(getItemsToDisplay(3, items, 1, 0, 2, 1)) # Output: ["item3"]
print(getItemsToDisplay(3, items, 0, 0, 2, 1)) # Output: ["item3"]
print(getItemsToDisplay(3, items, 2, 0, 2, 1)) # Output: ["item1"]
print(getItemsToDisplay(3, items, 2, 0, 2, 2)) # Output: []
print(getItemsToDisplay(3, items, 1, 0, 2, 0)) # Output: ["item2", "item1"]
print(getItemsToDisplay(3, items, 0, 0, 1, 2)) # Output: ["item3", "item1", "item2"]