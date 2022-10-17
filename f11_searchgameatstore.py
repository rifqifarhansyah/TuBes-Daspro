from A_CSV import *
from A_Functions import *


# F11
# kamus
# data : list of list of string
# id, nama, harga, kategori, tahun : string
# data_id , data_nama , data_harga , data_kategori , data_tahun : list of list of string
# total : list of list of string
# hasil : list of list of string
# hasil_id, hasil_nama, hasil_harga, hasil_kategori, hasil_tahun : list of list of string
# akhir : list of list of string

def search_game_at_store(data):

    id = input("Masukkan ID Game: ")
    if id != '':
        data_id = search_cat('id', id, data)
    else:
        data_id = []
    nama = input("Masukkan Nama Game: ")
    if nama != '':
        data_nama = search_cat('nama', nama, data)
    else:
        data_nama = []
    harga = input("Masukkan Harga Game: ")
    if harga != '':
        data_harga = search_cat('harga', harga, data)
    else:
        data_harga = []
    kategori = input("Masukkan Kategori Game: ")
    if kategori != '':
        data_kategori = search_cat('kategori', kategori, data)
    else:
        data_kategori = []
    tahun = input("Masukkan Tahun Rilis Game: ")
    if tahun != '':
        data_tahun = search_cat('tahun_rilis', tahun, data)
    else:
        data_tahun = []

    total = data_id + data_nama + data_harga + data_kategori + data_tahun
    hasil = []

    if total == []:
        print("Tidak ada game yang ditemukan.")
    else:
        hasil_id = no_duplicate(data_id, total, 0)

        hasil_nama = no_duplicate(data_nama, total, 1)

        hasil_harga = no_duplicate(data_harga, total, 4)

        hasil_kategori = no_duplicate(data_kategori, total, 2)

        hasil_tahun = no_duplicate(data_tahun, total, 3)

        hasil = hasil_id + hasil_nama + hasil_harga + hasil_kategori + hasil_tahun
        akhir = []


        if id != '':
            akhir = no_duplicate(hasil_id, hasil, 0)
            if nama != '':
                akhir = remove_not_match(akhir, nama, 1)
            if harga != '':
                akhir = remove_not_match(akhir, harga, 4)
            if kategori != '':
                akhir = remove_not_match(akhir, kategori, 2)
            if tahun != '':
                akhir = remove_not_match(akhir, tahun, 3)


        elif nama != '':
            akhir = no_duplicate(hasil_nama, hasil, 1)
            # if id != '':
            #     akhir = remove_not_match(akhir, id, 0)
            if harga != '' :
                akhir = remove_not_match(akhir, harga, 4)
            if kategori != '' :
                akhir = remove_not_match(akhir, kategori, 2)
            if tahun != '' :
                akhir = remove_not_match(akhir, tahun, 3)


        elif harga != '':
            akhir = no_duplicate(hasil_harga, hasil, 4)
            # if id != '':
            #     akhir = remove_not_match(akhir, id, 0)
            # if nama != '':
            #     akhir = remove_not_match(akhir, nama, 1)
            if kategori != '':
                akhir = remove_not_match(akhir, kategori, 2)
            if tahun != '' :
                akhir = remove_not_match(akhir, tahun, 3)
            

        elif kategori != '':
            akhir = no_duplicate(hasil_kategori, hasil, 2)
            # if id != '':
            #     akhir = remove_not_match(akhir, id, 0)
            # if nama != '':
            #     akhir = remove_not_match(akhir, nama, 1)
            # if harga != '' :
            #     akhir = remove_not_match(akhir, harga, 4)
            if tahun != '' :
                akhir = remove_not_match(akhir, tahun, 3)


        elif tahun != '':
            akhir = no_duplicate(hasil_tahun, hasil, 3)
            # if id != '':
            #     akhir = remove_not_match(akhir, id, 0)
            # if nama != '':
            #     akhir = remove_not_match(akhir, nama, 1)
            # if harga != '' :
            #     akhir = remove_not_match(akhir, harga, 4)
            # if kategori != '' :
            #     akhir = remove_not_match(akhir, kategori, 2)
            
        print("Daftar game pada inventory yang memenuhi kriteria:")
        if akhir == []:
            print("Game tidak ditemukkan.")
        else:
            for i in range(len(akhir)):
                print(i+1,".",akhir[i][0],"|",akhir[i][1],"|",akhir[i][2],"|",akhir[i][3],"|",akhir[i][4])