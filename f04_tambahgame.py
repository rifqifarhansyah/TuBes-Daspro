from A_CSV import *
from A_Functions import *

def tambah_game(data_game):
    count = 0
    while count < 5:
        count = 0
        nama_game = input('Masukkan nama game: ')
        if nama_game != '':
            count += 1
        kategori = input('Masukkan kategori: ')
        if kategori != '':
            count += 1
        tahun_rilis = input('Masukkan tahun rilis: ')
        if tahun_rilis != '':
            count += 1
        harga = input('Masukkan harga: ')
        if harga != '':
            count += 1
        stok = input('Masukkan stok awal: ')
        if stok != '':
            count += 1
        if count < 5:
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan di BNMO')

    id_game = 'G' + '0' + str(len(data_game)+1)
    data_tambah_game = [[id_game] + [nama_game] + [kategori] + [tahun_rilis] + [harga] + [stok]]

    data_tambah_game = [[id_game]+[nama_game] + [kategori] + [tahun_rilis] + [harga] + [stok]]
    data_game += data_tambah_game
    print('Selamat! Berhasil menambahkan game' + nama_game)
    return data_game

    
