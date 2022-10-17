def tictactoe():
    # KAMUS LOKAL
    # T : array of array of char
    # cek : bool
    # baris, kolom : int

    # ALGORITMA
    T = [['-' for j in range(3)] for i in range(3)]
    print("""
Daftar Pemain:
O Pemain 1
X Pemain 2
""")

    for i in range(3):
        for j in range(3):
         print(T[i][j], end = " ")
        print("")

    cek = True 

    giliran = 1

    while cek:
        if giliran%2 == 0 :
            urutan_pemain = "X"
        elif giliran%2 != 0 :
            urutan_pemain = "O"

        print(f"\nGiliran pemain {urutan_pemain}")
        baris = int(input("Baris: "))
        kolom = int(input("Kolom: "))

        while not ((1<= baris <= 3) or (1<=kolom<=3)):
            print("\nKotak tidak valid.")
            print(f"\nGiliran pemain {urutan_pemain}")
            baris = int(input("Baris: "))
            kolom = int(input("Kolom: "))

        while not (T[baris-1][kolom-1]=="-"):
            print("\nKotak sudah terisi. Silahkan pilih kotak lain.")
            print(f"\nGiliran pemain {urutan_pemain}")
            baris = int(input("Baris: "))
            kolom = int(input("Kolom: "))

        T[baris-1][kolom-1] = urutan_pemain

        print("\nStatus Papan")
        for i in range(3):
            for j in range(3):
                print(T[i][j], end = " ")
            print("")

        giliran += 1

        for i in range(3):
            if T[i][0]=="X":
                if T[i][1]=="X" and T[i][2]=="X":
                    cek = False
                    pemenang = "X"
            elif T[i][0] == "O":
                if T[i][1]=="O" and T[i][2]=="O":
                    cek = False
                    pemenang = "O"

        for j in range(3):
            if T[0][j]=="X":
                if T[1][j]=="X" and T[2][j]=="X":
                    cek = False
                    pemenang = "X"
            elif T[0][j] == "O":
                if T[1][j]=="O" and T[2][j]=="O":
                    cek = False
                    pemenang = "O"

        if T[1][1] == "X":
            if T[0][0]=="X" and T[2][2]=="X":
                cek = False
                pemenang = "X"
            elif T[0][2]=="X" and T[2][0]=="X":
                cek = False
                pemenang = "X"  
        elif T[1][1] == "O":
            if T[0][0]=="O" and T[2][2]=="O":
                cek = False
                pemenang = "O"
            elif T[0][2]=="O" and T[2][0]=="O":
                cek = False
                pemenang = "O"  

        if giliran == 10:
            cek = False
            pemenang = "None"
    
    if pemenang == "O" or pemenang == "X":
        print(f'\nPemain "{pemenang}" menang')
    else : print("Hasil Permainan Imbang")
