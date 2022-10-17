from A_CSV import *
from A_Functions import *

def login(data_user,user_id):
    if user_id != 0:
        user_name = input('Masukkan username: ')
        pword = input('Masukkan password: ')

        for line in data_user:
            data = line
            data_uname = data[2]
            data_pword = data[3]
            data_nama = data[1]
            id_user = data[0]
            role = data[4]
            
            count_true = 0
            if (user_name == data_uname) and (pword == data_pword):
                count_true += 1
                break
            
        #verifikasi login
        if count_true == 1:
            print('Halo ' + data_nama + '! Selamat datang di "Binomo"' )
        else:
            print('Password atau username salah atau tidak ditemukan.')
                
        return id_user, role

    else:
        print("Mohon exit terlebih dahulu untung logout dari akun.")
        return user_id, 'none'

