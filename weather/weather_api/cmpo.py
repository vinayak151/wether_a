import datetime

def is_prime(n):
    # Number is prime or not
    if n==1 or n==0:
        return False 
    return len([i for i in range(2,n) if n%i==0]) < 1

def date_int():
    date_list = str(datetime.date.today()).split('-')
    date_list = list(map(int,date_list))
    return date_list[2]

def is_dateprime():
    return is_prime(date_int())



