# WRITE YOUR SOLUTION HERE:
import re
def most_common_words(filename: str, lower_limit: int) -> dict:
    word_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.strip().split():
                word = re.sub(r'[^a-zA-Z0-9 ]', '', word)
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    return {k: v for k, v in word_dict.items() if v >= lower_limit}
            