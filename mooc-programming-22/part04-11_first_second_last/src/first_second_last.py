# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1] 
if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))