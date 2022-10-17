from A_CSV import *
from A_Functions import *


def list_game_toko(data_game):
    # KAMUS LOKAL
    # filterlist : string
    # banyakbaris : int

    # ALGORITMA
    filterlist = input("Skema sorting: ")
    banyakbaris = length_manual(data_game)
    if filterlist == "tahun+":
        print_matrix(filter_tahun_plus(data_game, banyakbaris))
    elif filterlist == "tahun-":
        print_matrix(filter_tahun_minus(data_game, banyakbaris))
    elif filterlist == "harga+":
        print_matrix(filter_harga_plus(data_game, banyakbaris))
    elif filterlist == "harga-":
        print_matrix(filter_harga_minus(data_game, banyakbaris))
    elif filterlist == "":
        print_matrix(data_game)
    else:
        print("Skema sorting tidak valid!")


def filter_tahun_plus(matriks, banyakbaris):
    # KAMUS LOKAL

    # ALGORITMA
    for i in range(1, banyakbaris-1):
        itahunmin = i
        tahunmin = int(matriks[itahunmin][3])
        for j in range(i+1, banyakbaris):
            if int(matriks[j][3]) < tahunmin:
                itahunmin = j
                tahunmin = int(matriks[j][3])
        temp = matriks[i]
        matriks[i] = matriks[itahunmin]
        matriks[itahunmin] = temp
    return matriks


def filter_tahun_minus(matriks, banyakbaris):
    # KAMUS LOKAL

    # ALGORITMA
    for i in range(1, banyakbaris - 1):
        itahunmax = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][3]) > int(matriks[itahunmax][3]):
                itahunmax = j
        temp = matriks[i]
        matriks[i] = matriks[itahunmax]
        matriks[itahunmax] = temp
    return matriks


def filter_harga_plus(matriks, banyakbaris):
    # KAMUS LOKAL

    # ALGORITMA
    for i in range(1, banyakbaris - 1):
        ihargamin = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][4]) < int(matriks[ihargamin][4]):
                ihargamin = j
        temp = matriks[i]
        matriks[i] = matriks[ihargamin]
        matriks[ihargamin] = temp
    return matriks


def filter_harga_minus(matriks, banyakbaris):
    # KAMUS LOKAL

    # ALGORITMA
    for i in range(1, banyakbaris - 1):
        ihargamax = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][4]) > int(matriks[ihargamax][4]):
                ihargamax = j
        temp = matriks[i]
        matriks[i] = matriks[ihargamax]
        matriks[ihargamax] = temp
    return matriks
