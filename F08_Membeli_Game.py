from A_CSV import *
from A_Functions import *
import datetime

def buy_game(id_user, data_game,data_user, data_kepemilikan, data_riwayat):
    # KAMUS LOKAL
    # id_game : string
    # data_game, data_riwayat, data_user : matrix hasil parsing
    # cek : bool
    id_game = str(input("Masukkan ID Game: "))
    # data_game = CSV_Parser("database/game.csv")
    # data_riwayat = CSV_Parser("database/riwayat.csv")
    # data_user = CSV_Parser("database/user.csv")
    cek = False
    # ALGORITMA UTAMA
    for i in range(length_manual(data_game)):
        if data_game[i][0] == id_game:
            index_game = i
            nama_game = data_game[i][1]
            if int(data_game[i][5]) < 0:
                print("Stok Game tersebut sedang habis!")
                cek = False
                return data_game,data_user, data_kepemilikan, data_riwayat
            else:
                cek = True

    for i in range(length_manual(data_riwayat)):
        if data_riwayat[i][3] == id_user and data_game[i][0] == id_game:
            print("Anda sudah memiliki Game tersebut!")
            cek = False
            return data_game,data_user, data_kepemilikan, data_riwayat
        else:
            cek = True

    for i in range(length_manual(data_game)):
        if data_game[i][0] == id_game:
            harga_game = int(data_game[i][4])
            break

    for i in range(length_manual(data_user)):
        if data_user[i][0] == id_user:
            index_user = i
            saldo_user = int(data_user[i][5])
            break

    if harga_game > saldo_user:
        print("Saldo anda tidak cukup untuk membeli game tersebut!")
        cek = False
        return data_game,data_user, data_kepemilikan, data_riwayat
    else:
        cek = True

    if cek:
        print(f"Game {nama_game} berhasil dibeli!")
        saldo_user -= harga_game
        data_game[index_game][5] = str(int(data_game[index_game][5]) - 1)
        data_user[index_user][5] = str(saldo_user)
        data_kepemilikan = data_kepemilikan + [[id_game]+ [id_user]]
        data_riwayat = data_riwayat + [[id_game] + [nama_game] + [str(harga_game)] + [id_user] + [str(datetime.datetime.now().strftime("%Y"))]]
        return data_game, data_user, data_kepemilikan, data_riwayat
        
