# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str) -> str:
    return "".join(list(filter(lambda x: x not in forbidden, string)))
