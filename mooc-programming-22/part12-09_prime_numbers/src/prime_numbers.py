# Write your solution here
def prime_numbers():
    i = 2
    while i > 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            yield i
        i += 1

# numbers = prime_numbers()
# for i in range(8):
#     print(next(numbers)) 
