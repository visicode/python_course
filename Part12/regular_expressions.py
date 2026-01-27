# Write your solution here
import re

def is_dotw(ins: str)->bool:
    return None != re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", ins)

def all_vowels(ins: str)->bool:
    return None != re.search("^[aieou]*$",ins)

def time_of_day(ins: str)->bool:
    return None != re.search("^[01][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]$",ins)
