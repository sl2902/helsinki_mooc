# Write your solution here
def store_personal_data(person: tuple) -> None:
    with open('people.csv', 'a') as w:
        w.write(";".join(str(s) for s in person) + "\n")

# store_personal_data(("Paul Paulson", 37, 175.5))
    
