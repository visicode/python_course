# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dl: list)->list:
    res=[]

    for i in dl:
        res.append(i.year)
    
    res.sort()

    return res

if __name__ == '__main__':
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
    #[1993, 2006, 2019]