import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = lower_case.upper()
num = '1234567890'
symbol = '!@#$%^&*_+?:;'

get_passwd = upper_case + lower_case + num  + symbol

lenght = 8
p = 0

for i in range (0,10):
    p += 1
    passwd = "".join(random.sample(get_passwd, lenght))
    print(f"Passdwd {p}:", passwd)
 
