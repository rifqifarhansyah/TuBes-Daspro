import f02_register as f02
import f03_login as f03
import f04_tambahgame as f04
import f05_ubahgame as f05
import f06_ubahstok as f06
import F07_Listing_Game as f07
import F08_Membeli_Game as f08
import F09_MelihatGameYangDimiliki as f09
import f10_searchmygame as f10
import f11_searchgameatstore as f11
import f12_topup as f12
import f13_riwayat as f13
import f14_help as f14
import f16_save as f16
import f15_load as f16_save
import f17_exit as f17
import B02_kerangajaib as b02
import B03_GameTictactoe as b03

# Kamus
# data_game, data_user, data_riwayat, data_kepemilikan : list of list of string
# user_id : string
# role : string
# menu : string

# Algoritma Utama

if __name__ == "__main__":              # program dijalankan langsung

    # men-load data dari sebuah folder
    data_game = f16_save.load("game.csv")
    data_user = f16_save.load("user.csv")
    data_riwayat = f16_save.load("riwayat.csv")
    data_kepemilikan = f16_save.load("kepemilikan.csv")

    print("loading ... ")

    print("Selamat datang di antarmuka \"Binomo\"!")

    # deklarasi user yang belum login
    user_id = '0'
    role = 'none'

    # loop dari menu
    while True:

        # input menu
        menu = input(">>> ")

        if menu == 'login':
            user_id, role = f03.login(data_user,user_id)

        elif menu == 'help':
            f14.help(role)
            
        elif menu == 'exit':
            f17.exit_program(data_game,data_user,data_riwayat,data_kepemilikan)

        elif menu == "kerangajaib":
            b02.kerang_ajaib()

        elif menu == "tictactoe":
            b03.tictactoe()

        # menu untuk user yang sudah login
        if user_id != '0':

            # menu untuk Admin
            if role.lower() == 'admin':

                if menu == 'register':
                    data_user = f02.register(data_user)

                if menu == 'tambah_game':
                    data_game = f04.tambah_game(data_game)
                    
                elif menu == 'ubah_game':
                    data_game = f05.ubah_game(data_game)

                elif menu == 'ubah_stok':
                    data_game = f06.ubah_stok(data_game)

                elif menu == 'topup':
                    data_user = f12.topup(data_user)
                
            # menu untuk user yang sudah login
            if menu == 'list_game_toko':
                f07.list_game_toko(data_game)
            
            elif menu == 'buy_game':
                data_game, data_user, data_kepemilikan, data_riwayat = f08.buy_game(user_id,data_game,data_user,data_kepemilikan,data_riwayat)
                
            elif menu == 'list_game':
                f09.melihat_game_user(user_id,data_riwayat,data_game)
                
            elif menu == 'search_my_game':
                f10.search_my_game(data_game,data_kepemilikan,user_id)
                
            elif menu == 'search_game_at_store':
                f11.search_game_at_store(data_game)
                
            elif menu == 'riwayat':
                f13.lihat_riwayat(user_id,data_riwayat)
                
            elif menu == 'save':
                f16.save_data(data_game,data_user,data_riwayat,data_kepemilikan)
            
            # elif menu == 'load':
            #     data_game = f15.load("game.csv")
            #     data_user = f15.load("user.csv")
            #     data_riwayat = f15.load("riwayat.csv")
            #     data_kepemilikan = f15.load("kepemilikan.csv")
            #     menu = input(">>> ")

else:
    print("Mohon jalankan program dari file utama.")
