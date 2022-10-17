## Rifqi
def length_manual(list):
    # KAMUS LOKAL
    # list : list
    # length : int

    # ALGORITMA
    length = 0                  
    for i in (list):
        length += 1
    return length

def append_manual(list_awal, item_baru):
    # KAMUS LOKAL
    # list_awal : list
    # item_baru : str, int, float, list
    # length_list_awal, indeks_terakhir : int
    # list_baru : list

    # ALGORITMA
    length_list_awal = length_manual(list_awal)
    list_baru = [0 for i in range(length_list_awal + 1)]
    for i in range(length_list_awal):
        list_baru[i] = list_awal[i]
    indeks_terakhir = length_list_awal
    list_baru[indeks_terakhir] = item_baru
    return list_baru

def split_manual(list_awal, pemisah):
    # KAMUS LOKAL
    # List_awal : list
    # pemisah : char

    # ALGORITMA
    list_baru = []
    item = ''
    for i in list_awal:
        if i == pemisah:
            list_baru = append_manual(list_baru, item)  
            item = ''                                   
        else:
            item += i                                   
    list_baru = append_manual(list_baru, item)
    return(list_baru)

def remove_manual(list_awal, index):
    # KAMUS LOKAL
    # list_baru : list
    # index : int

    # ALGORITMA
    list_baru = []
    for i in range(length_manual(list_awal)):
        if i != index:
            list_baru = append_manual(list_baru,list_awal[i])
    return list_baru

def max_length(data,kolom):
    # KAMUS LOKAL
    # max : int

    # ALGORITMA
    max = length_manual(data[0][kolom])
    for i in range(length_manual(data)):
        if length_manual(data[i][kolom])> max:
            max = length_manual(data[i][kolom])
    return max

def print_matrix(matrix):
    # KAMUS LOKAL
    # baris : int
    # kolom : int
    # maxlencolumn : array of int

    # ALGORITMA
    baris = length_manual(matrix)
    kolom = length_manual(matrix[0])
    maxlencolumn = [0 for i in range(kolom+1)]
    maxlencolumn[0] = length_manual(str(baris-1))
    for i in range(kolom):
        maks = length_manual(matrix[1][i])
        for j in range(2, baris):
            if maks < length_manual(matrix[j][i]):
                maks = length_manual(matrix[j][i])
        maxlencolumn[i+1] = maks

    for i in range(1, baris):
        print(str(i) + "." + (" " * (maxlencolumn[0] - length_manual(str(i)))), end=" ")
        for j in range(kolom):
            data = matrix[i][j]
            if (j+1) != kolom:
                print(data + (" " * (maxlencolumn[j + 1] - length_manual(data))), end=" | ")
            else:
                print(data + (" " * (maxlencolumn[j + 1] - length_manual(data))))


#### Nayya

def len(data):
    count = 0
    for i in data:
        count += 1
    return count

def inside(element,list):
    for i in range(len(list)):
        if element == list[i]:
            return True
    return False
    
def split(string, delimiters= ';'):
    x = []
    word = ''
    for s in string:
        if s not in delimiters:
            word = word + s
        elif word:
            x = x +[word]
            word = ''
    if word:
        x = x + [word]
    return x    

### Sano
# fungsi pembantu
# Kamus
# count : integer
# data : list of list of string
def len(data):
    count = 0
    for i in data:
        count += 1
    return count

# kamus
# elemen, list : list of list of string
def inside(element,list):
    for i in range(len(list)):
        if element == list[i]:
            return True
    return False

# kamus
# list : list of list of string
# index : integer
def pop(list,index):
    temp = []
    for i in range(len(list)):
        if i != index:
            temp = temp + [list[i]]
    return temp

# kamus
# list1,list2 : list of list of string
# hasil : list of list of string
# index : integer
def no_duplicate(list1,list2,index):
    hasil = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i][index] == list2[j][index]:
                if not(inside(list1[i],hasil)):
                    hasil = hasil + [list1[i]]
    return hasil

# kamus
# data : list of list of string
# category : string
# name : string
def search_cat(category, name, data):
    hasil = []
    for i in range(len(data[0])):
        if data[0][i] == category:
            for j in range(len(data)):
                if name == data[j][i]:
                    hasil = hasil + [data[j]]
    return hasil


# kamus
# data : list of list of string
# category : string
# name : string
def search_in(index, name, data):
    hasil = []
    for j in range(len(data)):
        if name == data[j][index]:
            hasil = hasil + [data[j]]
    return hasil


# kamus
# data : list of list of string
# elemen : string
# index : integer
def remove_not_match(data,element,index):
    for i in range(len(data)):
        if data[i][index] != element:
            data = pop(data,i)
    return data

