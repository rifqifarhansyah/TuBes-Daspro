from A_CSV import *
from A_Functions import *

def melihat_game_user(id_user, data_riwayat, data_game):
    # KAMUS LOKAL
    # data_riwayat, data_game : matrix hasil parsing
    # properti_game : array
    # data_game_user : matrix hasil

    # data_riwayat = CSV_Parser('database/riwayat.csv')
    # data_game = CSV_Parser('database/game.csv')

    data_game_user = []
    properti_game = []
    # ALGORITMA UTAMA
    for i in range(length_manual(data_riwayat)):
        if data_riwayat[i][3]== id_user:
            game_id_dipunya = data_riwayat[i][0]
            for j in range(length_manual(data_game)):
                if data_game[j][0] == game_id_dipunya:
                    for k in range(length_manual(data_game[j])):
                        properti_game = append_manual(properti_game, data_game[j][k])
                    data_game_user = append_manual(data_game_user, properti_game)
                    properti_game = []
    if data_game_user==[]:
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        print_matrix(data_game_user)
    
