import os,time,pwinput
from prettytable import PrettyTable

user = {
    "nama":["ibnu","alfarezi"],
    "password":["ibnu","alfarezi"],
    "namaAdmin":["ibnu","alfarezi"],
    "passwordAdmin":["admin","admin1"]
}
menu = {
    "isi" : ["butter","jagung"],
    "harga" : [1000,2000]
}

tbM = PrettyTable(["Nama Menu","Harga"]) 
tbM.title = "Toko Ibnu Al-Farezi"



def showData():
    tbM.clear_rows()
    for i in range(len(menu.get("isi"))):
        tbM.add_row([menu.get("isi")[i],menu.get("harga")[i]])
    print(tbM)

def clear():
    os.system('cls')
    time.sleep(1)

def menuAdmin():
    while True:
        print(" ="*15,"\n1.Hapus\n2.Liat Stok\n3.Update\n4.Buat barang\n5.Kembali\n"," ="*15)
        pilih = input("Masukan Pilihan -> ")
        if pilih == "1":
            clear()
            showData()
            hapus = input("Masukan Nama Menu yang ingin dihapus ->  ")
            if hapus in menu.get("isi"):
                index = menu.get("isi").index(hapus)
                menu.get("isi").remove(hapus)
                menu.get("harga").pop(index)
                print("Menu Berhasil Dihapus")
            else:
                clear()
                print("Data Tidak Di Temukan")  
        elif pilih == "2":
            clear()
            showData()
        elif pilih == "3":
            nama = input("Masukan Menu Yang Ingin Diganti -> ")
            if nama in menu.get("isi"):
                update = input("Masukan Nama Menu Baru ->  ")
                while True:
                    try:
                        updateH = int(input("Masukan Harga Menu Baru ->  "))
                        break
                    except:print("Gunakan Angka!!")
                index = menu.get("isi").index(nama)
                menu.get("isi")[index] = update
                menu.get("harga")[index]= updateH
                clear()
                print("Data Telah DiUbah")
            else:print("Nama Tidak Ditemukan")
        elif pilih == "4":
            clear()
            nama = input("Masukan Nama Menu -> ")
            while True:
                try:
                    harga = int(input("Masukan Harga -> "))
                    break
                except:print("Input Menggunakan Angka")
            if nama in menu.get("isi"):print("Nama Menu Sudah Ada Masukan Nama Lain")
            else:
                clear()
                menu.get("isi").append(nama)
                menu.get("harga").append(harga)
                showData()
                print("Berhasil Nambah Menu Baru")
        elif pilih == "5":
            clear()
            break
        else:
            clear()
            print("Masukan Dengan Benar!")

def menuUser():
    print(" ="*15,"\n1.Beli Barang\n2.Liat barang\n"," ="*15)
    pilih = input("Masukan Pilihan -> ")
    if pilih == "1":
            clear()
            showData()
            pilih = input("Masukan Nama Menu Yang Ingin Dibeli -> ")
            index = menu.get("isi").index(pilih)
            if pilih in menu.get("isi"):
                while True:
                    try:
                        jumlah = int(input("Masukan Jumlah Yang Ingin Dibeli -> "))
                        break
                    except: print("Masukan Dengan Angka!")
                total = menu.get("harga")[index] * jumlah
                print("Anda Membeli Nama Menu -> {}\nHarga -> {}".format(pilih,total))
            else:print("Nama Menu Tidak Tersedia")
    elif pilih == "2":
        clear()
        showData()
    else:print("Masukan Dengan Benar!")

while True:
    print(" ="*15,"\n\t1.Login Admin\n\t2.Login User\n\t3.Register User\n"," ="*15)
    pilih = input("Masukan pilihan -> ")
    if pilih == "1":
        try:
            nama = input("Masukan UserName -> ")
            pw = pwinput.pwinput(prompt='Masukan Password: ')
            idx = user.get("namaAdmin").index(nama)
            if nama == user.get("namaAdmin")[idx] and pw == user.get("passwordAdmin")[idx]:
                print("Login berhasil")
                clear()
                menuAdmin()
                continue
            else:
                clear()
                print("Login Gagal Masukan Ulang")
                continue
        except ValueError:
            clear()
            print("Nama  Tidak Ditemukan!!")
            continue
        
    elif pilih == "2":
        try:
            nama = input("Masukan UserName -> ")
            pw = pwinput.pwinput(prompt='Masukan Password: ')
            idx = user.get("nama").index(nama)
            if nama == user.get("nama")[idx] and pw == user.get("password")[idx]:
                print("Login berhasil")
                clear()
                menuUser()
                ulang = input("Kembali y/n : ").lower()
                if ulang == "y":
                    clear()
                    continue
                else:break
            else:
                clear()
                print("Login Gagal Masukan Ulang")
        except ValueError:
            clear()
            print("Nama  Tidak Ditemukan")
    elif pilih == "3":
        while True:
            namaBaru = input("UserName Baru: ")
            pwBaru = pwinput.pwinput(prompt='Masukan Password: ')
            if namaBaru in user.get("nama") and pwBaru in user.get("password"):
                print("Nama Sudah Tersedia!")
            else:
                clear()
                user.get("nama").append(namaBaru)
                user.get("password").append(pwBaru)
                print("Berhasil Buat Akun")
                break
        time.sleep(1)
        clear()    
        continue
    else:
        clear()
        print("Tidak Tersedia")