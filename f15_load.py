import argparse
import os
from A_CSV import *
from A_Functions import *

# F16
# kamus
# folder, file : string
def load(filename):
    # args
    parser = argparse.ArgumentParser(exit_on_error=False)
    parser.add_argument("folder", help="Masukkan folder yang akan di-load yang berlokasi sama dengan file.")
    # error message
    try:
        parser.parse_args()
    except:
        print("Tidak ada nama folder yang diberikan!")
        exit()
    args = parser.parse_args()


    # folder yang ada di lokasi file
    list_folder = os.listdir('.')
    found = False

    # mengecek apakah folder yang diberikan ada di lokasi file
    for i in range(len(list_folder)):
        if list_folder[i] == args.folder:
            found = True
            break
    if not(found):
        print("Folder",args.folder,"tidak ditemukan.")
        exit()
    return  read_csv(args.folder + '//' +filename)

    