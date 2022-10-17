from A_CSV import *
from A_Functions import *

# F06
def ubah_stok(data_game):
    id = input("Masukkan ID game: ")
    stok = input("Masukkan jumlah: ")
    found = False  
    
    try:
        int(stok)
    except:
        print("Stok harus berupa angka")
        return data_game

    stok = int(stok)
    if stok == '':
        print("Stok tidak boleh kosong!")
        return data_game

    if id != '':
        for i in range(len(data_game)):
            if id == data_game[i][0]:
                if stok >= 0:
                    data_game[i][5] = str(int(data_game[i][5]) + stok)
                    print("Stok game",data_game[i][1],"berhasil ditambah. Stok sekarang:", data_game[i][5])
                    
                else:
                    if abs(stok) <= int(data_game[i][5]):
                        data_game[i][5] = str(int(data_game[i][5]) + stok)
                        print("Stok game",data_game[i][1],"berhasil dikurang. Stok sekarang:", data_game[i][5])
                        
                    else:
                        print("Stok game",data_game[i][1],"gagal dikurang karena stok kurang. Stok sekarang:", data_game[i][5],'( <',str(abs(stok)),')')
                found = True  
            
           
        if not found:
            print("Tidak ada id tersebut.")

    else:
        print("ID tidak boleh kosong.")

    return data_game

