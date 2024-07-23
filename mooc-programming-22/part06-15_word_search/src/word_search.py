# Write your solution here
import re
def find_words(search_term: str) -> list:
    found = []
    with open('words.txt') as f:
        for word in f:
            word = word.strip()
            idx_star = search_term.find('*')
            idx_dot = re.findall(r'\.', search_term)
            print(idx_dot)
            if idx_star == 0:
                if word.endswith(search_term[idx_star+1:]):
                    found.append(word)
            elif idx_star > 0:
                if word.startswith(search_term[:idx_star]):
                    found.append(word)
            elif len(idx_dot) > 0:
                if re.search(search_term, word) and len(word) == len(search_term):
                    found.append(word)
            else:
                if search_term == word:
                    found.append(word)
    return found

# print(find_words("*vokes"))
# print(find_words("ca."))
