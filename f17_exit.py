import f16_save as f16

def exit_program(data_game, data_user, data_riwayat, data_kepemilikan):
    print('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    x = input('>>> ')

    if (x == 'Y') or (x == 'y'):
        f16.save_data(data_game,data_user,data_riwayat,data_kepemilikan)
        print('Sampai jumpa!')
        exit()
    elif (x == 'N') or (x == 'n'):
        print('Sampai jumpa!')
        exit()
        
    while not ((x == 'Y') or (x == 'y') or (x == 'n') or (x == 'N')):
        print('Input tidak valid.')
        print('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
        x = input('>>> ')
        if (x == 'Y') or (x == 'y'):
            f16.save_data(data_game,data_user,data_riwayat,data_kepemilikan)
            print('Sampai jumpa!')
            exit()
        elif (x == 'N') or (x == 'n'):
            print('Sampai jumpa!')
            exit()
    

