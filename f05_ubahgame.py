from A_CSV import *
from A_Functions import *


#  F05
def ubah_game(data_game):
    id = input("Masukkan ID game: ")
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori game: ")
    tahun_rilis = input("Masukkan tahun rilis game: ")
    harga = input("Masukkan harga game: ")

    if id != '':
        for i in range(len(data_game)):
            if id == data_game[i][0]:
                if nama != '':
                    data_game[i][1] = nama
                if kategori != '':
                    data_game[i][2] = kategori
                if tahun_rilis != '':
                    data_game[i][3] = tahun_rilis
                if harga != '':
                    data_game[i][4] = harga
                print("Game berhasil diubah")
                found = True
        if not found:
            print("Tidak ada id tersebut.")
    else:
        print("ID tidak boleh kosong.")

    return data_game