# Write your solution here
import re
def is_dotw(my_string: str):
    return True if re.search(r'^Mon|Tue|Wed|Thu|Fri|Sat|Sun$', my_string) else False

def all_vowels(my_string: str):
    return True if re.search(r'^[aeiouy]+$', my_string) else False

def time_of_day(my_string: str):
    return True if re.search(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', my_string) else False
# print(is_dotw("Mon"))
# print(is_dotw("Fri"))
# print(is_dotw("Tui"))

# print(all_vowels("eioueioieoieouyyyy"))
# print(all_vowels("autoooo"))

# print(time_of_day("12:43:01"))
# print(time_of_day("AB:01:CD"))
# print(time_of_day("17:59:59"))
# print(time_of_day("23:15:xx"))