from A_CSV import *
from A_Functions import *

def register(data_user):
    name = input('Masukkan nama: ')
    user_name = input('Masukkan username: ')
    pword = input('Masukkan password: ')
    illegal = "!@#$%^&*()+?=,.<>/\''"""

    count = 0
    for c in user_name:
        if inside(c, illegal):
            count += 1
    if count > 0:
        print ('Username harus terdiri atas alfabet, angka, _, dan -')

    ID = len(data_user)
    data_register = [str(ID)] + [name] + [user_name] + [pword] + ['User'] + ['0']

    count_false = 0
    for line in data_user:
        data = line
        data_uname = data[2]
        if user_name == data_uname:
            count_false += 1

    if count_false == 0:
        data_user += [data_register]
    else:
        print('Maaf! Username sudah dipakai.')

    return data_user



