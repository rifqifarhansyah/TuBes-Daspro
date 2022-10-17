import datetime

def lcg(m):

    time = datetime.datetime.now()

    hour = int(time.strftime("%H")) 
    min = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    mil_sec = int(time.strftime("%f"))

    a = hour * sec
    x = mil_sec
    c = min * sec

    return (((a * x)+ c) % m)

def kerang_ajaib():
    
    wisdom = ["Ya","Tidak","Bisa jadi","Tentunya","Tidak mungkin"
            ,"Mungkin suatu hari","Coba tanya lagi", "Tidak ada"]

    m = len(wisdom)

    num = lcg(m)

    input("Apa pertanyaanmu? ")
    print()
    print(wisdom[num])
    print()




