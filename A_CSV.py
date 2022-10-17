from A_Functions import *

## Rifqi
def CSV_Parser(nama_file_csv):
    # KAMUS LOKAL
    # nama_file_csv : CSV       
    # matriks_baru  : Matrix    

    # ALGORITMA
    matriks_baru = []
    with open(nama_file_csv, 'r', encoding='utf-8-sig') as file:
        for line in file:
            matriks_baru = append_manual(matriks_baru, split_manual(line.replace('\n',''),';')) 
    return(matriks_baru)

## Sano
# Read File
# filename: string
# seperator: string
# batas : integer
# data : list of list of string
# result : list of string
# word : string
# count : integer

def read_csv(filename):
    seperator = ";\n"

    with open(filename , 'r', encoding='utf-8-sig') as f:

        batas = 0
        for line in f.readline():
            for i in line:
                if inside(i,seperator):
                    batas += 1

    with open(filename , 'r', encoding='utf-8-sig') as f:

        data = []

        for line in f.readlines():
            result = []
            word = ''
            count = 0

            for c in line:
                if not(inside(c,seperator)):
                    word = word + c
    
                else:
                    result = result + [word]
                    word = ''
                    count += 1

            if count == batas:
                data = data + [result]

    return data

# kamus 
# filename : string
# data : list of list of string
def write_csv(filename, data):
    with open(filename, 'w') as f:

        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(data[i][j])

                if j != len(data[i]) - 1:
                    f.write(';')
                    
            f.write('\n')