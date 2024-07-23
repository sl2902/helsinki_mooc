# Write your solution here:
def sort_by_remaining_stock(items: list) -> list:
    def sort_by_stock(item: tuple):
        return item[2]
    return sorted(items, key=sort_by_stock)



