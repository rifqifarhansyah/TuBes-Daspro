from A_CSV import *
from A_Functions import *

# F10
# kamus
# data : list of list of string
# id , tahun: string
# data_id, data_tahun : list of list of string
# hasil : list of list of string
def search_my_game(data_game,data_kepemilikan,user_id):
    id = input("Masukkan ID Game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")

    id_game = []
    for i in range(len(data_kepemilikan)):
        if data_kepemilikan[i][1] == user_id:
            id_game = id_game + [data_kepemilikan[i][0]]
    
    my_games = []
    for i in range(len(id_game)):
        my_games = my_games + search_cat('id',id_game[i],data_game)


    if id != '' and tahun != '' :
        data_id = search_in(0, id, my_games)
        hasil = remove_not_match(data_id, tahun, 3)
        if hasil == []:
            print("Game tidak ditemukan")
        else:
            for i in range(len(hasil)):
                print(i+1,".",hasil[i][0],"|",hasil[i][1],"|",hasil[i][2],"|",hasil[i][3],"|",hasil[i][4])
            
    elif id != '':
        data_id = search_in(0, id, my_games)
        if data_id == []:
            print("Game tidak ditemukan")
        else:
            for i in range(len(data_id)):
                print(i+1,".",data_id[i][0],"|",data_id[i][1],"|",data_id[i][2],"|",data_id[i][3],"|",data_id[i][4])

    elif tahun != '':
        data_tahun = search_in(3, tahun, my_games)
        if data_tahun == []:
            print("Game tidak ditemukan")
        else:
            for i in range(len(data_tahun)):
                print(i+1,".",data_tahun[i][0],"|",data_tahun[i][1],"|",data_tahun[i][2],"|",data_tahun[i][3],"|",data_tahun[i][4])

    else:
        print("Tidak ada input yang dimasukkan.")