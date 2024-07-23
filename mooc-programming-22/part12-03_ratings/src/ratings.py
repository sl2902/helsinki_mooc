# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def sort_by_rating(item: dict):
        return item['rating']
    return sorted(items, key=sort_by_rating, reverse=True)
