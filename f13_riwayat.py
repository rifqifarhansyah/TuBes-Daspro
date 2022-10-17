from A_Functions import *
from A_CSV import *

def lihat_riwayat(user_id, data_riwayat):
    # KAMUS LOKAL
    # user_id : string
    # data_riwayat : matriks hasil parsing
    # panjang_riwayat : int
    # cek : bool

    # user_id = str(input('Masukan user id: '))
    # data_riwayat = CSV_Parser('riwayat.csv')

    panjang_riwayat = length_manual(data_riwayat)
    dipunya = 0
    cek = False
    # ALGORITMA UTAMA
    for i in range(panjang_riwayat):
        if data_riwayat[i][3] == user_id:
            dipunya+=1
            cek = True

    if cek == True:
        riwayatBeli = ['' for i in range(dipunya)]  # inisialisasi
        i = 0
        k = 0
        while i <= length_manual(data_riwayat):
            if data_riwayat[i][3] == user_id:  # apabila game dimiliki oleh user ID yg sama dengan yg ter log in,
                riwayatBeli[k] = data_riwayat[i]  # append game yang dimiliki oleh user di iterasi ke-i
                k += 1
            i += 1
        printmatrix(riwayatBeli)
    else:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.')