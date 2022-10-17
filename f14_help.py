from A_CSV import *
from A_Functions import *

def help(role):
    role_user = role

    print('======== HELP =======')

    if role_user.lower() == 'admin':
        print(' 1. register - untuk melakukan registrasi user baru.\n 2. login - untuk melakukan login ke sistem.\n 3. tambah_game - untuk menambahkan game ke toko\n 4. ubah_game - untuk mengubah game pada toko.\n 5. ubah_stok - untuk mengubah stok game di toko\n 6. list_game_toko - untuk melakukan sorting daftar game sesuai kategori tertentu.\n 7. search_game_at_store - untuk mencari game di toko.\n 8. topup - untuk menambahkan saldo user.\n 9. save - untuk melakukan penyimpanan pada file yang diubah.')
        
    else:
        print(' 1. login - untuk melakukan login ke sistem.\n 2. list_game_toko - untuk melakukan sorting pada game di toko sesuai kategori tertentu.\n 4. buy_game - untuk membeli game di toko.\n 5. list_game - untuk melihat game yang dimiliki user.\n 6. search_my_game - untuk mencari game yang dimiliki berdasarkan id dan tahun rilis.\n 7. search_game_at_store - untuk mencari game di toko berdasarkan kategori tertentu.\n 8. riwayat - untuk melihat riwayat pembelian.\n 9. save - untuk menyimpan perubahan pada file.')
    
    print(' 10. kerang_ajaib - untuk bertanya kepada kerang ajaib.')
    print(' 11. tictactoe - untuk bermain tic tac toe.')
    print('......................')
    

            

