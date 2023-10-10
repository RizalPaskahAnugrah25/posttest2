from prettytable import PrettyTable

# list untuk menyimpan data admin
data_admin = [
    {"username": "adminganteng", "password": "gacorrrkanggg"},
    {"username": "admincantik", "password": "rungkadddkanggg"}
]

while True:
    username = input("Masukkan Nama Anda: ")
    password = input("Masukkan NIM Anda: ")
    
    if not password.isdigit():
        print("NIM harus diisi dengan angka. Silakan coba lagi.")
        continue
    else:
        print("Selamat datang", username)
        break


# list untuk menyimpan data item
data_item = [
    ["001", "Netflix sharing premium 1 bulan", 21000],
    ["002", "Netflix private premium 1 bulan", 42000],
    ["003", "Disney sharing premium 1 bulan", 55000],
    ["004", "Disney private premium 1 bulan", 150000],
    ["005", "IQYI sharing premium 1 bulan", 10000],
    ["006", "IQYI private premium 1 bulan", 40000],
]

# pembeli
def transaksi():
    total_harga = 0
    while True:
        # menampilkan seluruh item yang tersedia
        print("Daftar Item yang Tersedia")
        show_item()
        
        # input id item dan jumlah yang ingin dibeli
        id_item = input("Masukkan ID item yang ingin dibeli atau 0 untuk selesai: ")
        if id_item == "0":
            # menampilkan total harga pembelian
            print("Total harga pembelian: Rp", total_harga)
            return
        qty = int(input("Masukkan jumlah yang ingin dibeli: "))
        
        # memeriksa apabila jumlah yang ingin dibeli melebihi stok
        for item in data_item:
            if item[0] == id_item:
                if qty <= 0:
                    print("Jumlah pembelian minimal adalah 1!")
                    break
                else:
                    total_harga += item[2] * qty
                    break
        else:
            print("ID item tidak ditemukan atau jumlah yang dimasukkan salah!")

# admin
def create():
    # input data item yang baru
    id_item = input("Masukkan ID item: ")
    nama_item = input("Masukkan nama item: ")
    harga_item = int(input("Masukkan harga item: "))
    
    # menambahkan item yang baru ke dalam database
    data_item.append([id_item, nama_item, harga_item])
    
    # menampilkan daftar item lengkap dengan item baru yang ditambahkan
    show_item()

def read():
    # menampilkan seluruh item yang terdapat dalam database
    show_item()

def update():
    # input id item yang ingin diperbarui
    id_item = input("Masukkan ID item yang ingin di-update data: ")
    for i in (len(data_item)):
        if data_item[i][0] == id_item:
            # input data item yang baru
            nama_item = input("Masukkan nama item baru: ")
            harga_item = int(input("Masukkan harga item baru: "))
            
            # melakukan update item yang dipilih
            data_item[i][1] = nama_item
            data_item[i][2] = harga_item
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Item tidak ditemukan")

def delete():
    # input id item yang ingin dihapus
    id_item = input("Masukkan ID item yang ingin dihapus: ")
    for i in (len(data_item)):
        if data_item[i][0] == id_item:
            # menghapus item sesuai input id
            data_item.pop(i)
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Item tidak ditemukan")
    
# menampilkan seluruh item yang terdapat dalam database dengan prettytable
def show_item():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Item", "Harga"]
    for item in data_item:
        table.add_row(item)
    print(table)

# program utama
while True:
    print("="*30)
    print("TOKO STREAMING")
    print("="*30)
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        print("="*30)
        print("ADMIN TOKO STREAMING")
        print("="*30)
        is_admin = False
        while not is_admin:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            for admin in data_admin:
                if admin["username"] == username and admin["password"] == password:
                    is_admin = True
                    break
            
            if not is_admin:
                print("Username atau password salah. Silakan coba lagi.")
        
        # tampilan menu admin
        print("1. Tambah Item")
        print("2. Lihat Item")
        print("3. Update Item")
        print("4. Hapus Item")
        print("5. Kembali")

        admin_choice = input("Pilih menu: ")
        if admin_choice == "1":
            create()
        elif admin_choice == "2":
            read()
        elif admin_choice == "3":
            update()
        elif admin_choice == "4":
            delete()
        elif admin_choice == "5":
            continue
        else:
            print("Menu tidak tersedia")

    elif choice == "2":
        print("="*30)
        print("PEMBELI")
        print("="*30)
        transaksi()
    elif choice == "3":
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    else:
        print("Menu tidak tersedia")
        