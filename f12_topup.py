from A_CSV import *
from A_Functions import *


def topup(data_user):
    user_name = input('Masukkan username: ')
    saldo = input('Masukkan saldo: ')

    try:
        int(saldo)
    except:
        print("Saldo harus berupa angka")
        return data_user
        
    saldo = int(saldo)
    index = 0
    for line in data_user:
        data = line
        data_id = data[0]
        data_name = data[1]
        data_uname = data[2]
        data_pword = data[3]
        data_role = data[4]
        data_saldo = data[5]

        if (user_name == data_uname):
            index = int(line[0])
            break

    saldo_before = int(data_saldo)
    saldo_after = saldo_before + saldo

    if (index != 0) and (saldo>0):
      data_user[index][5] = str(saldo_after)
      print("Top up berhasil. Saldo",data_name ,"bertambah menjadi", saldo_after) 
    elif(index != 0) and (saldo < 0) and (saldo_before >= saldo*-1):
      data_user[index][5] = str(saldo_after)
      print("Top up berhasil. Saldo",data_name ,"berkurang menjadi", saldo_after)
    elif (index != 0) and (saldo < 0) and ((saldo*-1) > saldo_before):
      print('Masukan tidak valid. Saldo Anda tidak mencukupi.')
    elif index == 0:
      print('Username ' + user_name + ' tidak ditemukan.')

    return data_user

    
