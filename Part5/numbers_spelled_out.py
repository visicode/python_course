# Write your solution here
def dict_of_numbers() -> dict:
    d={}
    d[0]='zero'
    d[1]="one"
    d[2]="two"
    d[3]="three"
    d[4]="four"
    d[5]="five"
    d[6]="six"
    d[7]="seven"
    d[8]="eight"
    d[9]="nine"
    d[10]="ten"
    d[11]="eleven"
    d[12]="twelve"
    d[13]="thirteen"
    d[14]="fourteen"
    d[15]="fifteen"
    d[16]="sixteen"
    d[17]="seventeen"
    d[18]="eighteen"
    d[19]="nineteen"
    d[20]="twenty"
    d[30]="thirty"
    d[40]="forty"
    d[50]="fifty"
    d[60]="sixty"
    d[70]="seventy"
    d[80]="eighty"
    d[90]="ninety"
    for i in range(9):
        d[20+i+1]=d[20]+'-'+d[i+1]
        d[30+i+1]=d[30]+'-'+d[i+1]
        d[40+i+1]=d[40]+'-'+d[i+1]
        d[50+i+1]=d[50]+'-'+d[i+1]
        d[60+i+1]=d[60]+'-'+d[i+1]
        d[70+i+1]=d[70]+'-'+d[i+1]
        d[80+i+1]=d[80]+'-'+d[i+1]
        d[90+i+1]=d[90]+'-'+d[i+1]
    return d


if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])