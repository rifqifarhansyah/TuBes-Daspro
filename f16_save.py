import os
from A_CSV import *
from A_Functions import *

# F15
 # kamus
 # data : list of list of string
 # file : string

def save(data,file,folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
        write_csv(folder + '//' +  file, data)

def save_data(data_game,data_user,data_riwayat,data_kepemilikan):
    folder = input("Masukkan nama folder penyimpanan: ")
    if folder != '':
        save(data_game,'game.csv',folder)
        save(data_user,'user.csv',folder)
        save(data_riwayat,'riwayat.csv',folder)
        save(data_kepemilikan,'kepemilikan.csv',folder)
        print("Saving ...")
        print("Data berhasil disimpan di folder", folder)
    else:
        print("Tidak ada input yang dimasukkan. Kembali ke menu.")

