# Write your solution here
size = int(input('How many items: '))
items = []
for i in range(size):
    item = int(input(f'Item{i+1}: '))
    items.append(item)
print(items)
