# Write your solution here
from datetime import *

def is_it_valid(pic: str)->bool:
    ret=True
    control="0123456789ABCDEFHJKLMNPRSTUVWXY"

    if len(pic)>11:
        return False

    if pic[6] not in ('-','+','A'):
        return False
        
    str_date = pic[:6]
    if not str_date.isdecimal():
        return False

    if pic[6] == '-':
        ye = 1900+int(pic[4:6])
    if pic[6] == '+':
        ye = 1800+int(pic[4:6])
    if pic[6] == 'A':
        ye = 2000+int(pic[4:6])

    #days should be between 1-31
    if 1>int(pic[:2])>31:
        return False
    #months should be 1-12
    if 1>int(pic[2:4])>12:
        return False
    #years can be 00-99 All OK

    mo=int(pic[2:4])
    da=int(pic[:2])

    try:
        test = datetime(ye,mo,da)
    except:
        return False

    str_ser = pic[7:10]
    if not str_ser.isdecimal():
        return False

    num = int(str_date+str_ser)
    ref = num%31
    if control[ref]!=pic[-1:]:
        return False

    return ret

if __name__ == '__main__':
    print(is_it_valid("230827-906F"))

#Examples
#    230827-906F
#    120488+246L
#    310823A9877
