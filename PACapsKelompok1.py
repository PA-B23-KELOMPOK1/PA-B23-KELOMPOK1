import mysql.connector
from getpass import getpass

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kelompok1"
)

cursor = db.cursor()
cursor.execute("USE kelompok1")
db.commit()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

def login_admin():
    nama_admin = input("Masukkan username: ")
    password = getpass("Masukkan password: ")
    query = "SELECT * FROM admin WHERE nama_admin = %s AND password = %s"
    cursor.execute(query, (nama_admin, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil sebagai admin.")
        return True
    else:
        print("Login gagal. Periksa kembali username dan password.")
        return False

def menu_admin():
    while True:
        print("\nPilihan Menu Admin:")
        print("1. Tambah data")
        print("2. Lihat data")
        print("3. Ubah data")
        print("4. Hapus data")
        print("5. Logout")
        pilihan_menu = input("Pilih menu: ")
        if pilihan_menu == '1':
            menu_tambah_data()
        elif pilihan_menu == '2':
            menu_lihat_data()
        elif pilihan_menu == '3':
            menu_ubah_data()
        elif pilihan_menu == '4':
            menu_hapus_data()
        elif pilihan_menu == '5':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def menu_tambah_data():
    while True:
        print("\nPilihan Tambah Data:")
        print("1. Produk")
        print("2. Petani")
        print("3. Kembali")
        pilihan_tambah = input("Pilih menu: ")
        if pilihan_tambah == '1':
            tambah_data_produk()
        elif pilihan_tambah == '2':
            tambah_data_petani()
        elif pilihan_tambah == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def menu_lihat_data():
    while True:
        print("\nPilihan Lihat Data:")
        print("1. Produk")
        print("2. Petani")
        print("3. Kembali")
        pilihan_lihat = input("Pilih menu: ")
        if pilihan_lihat == '1':
            lihat_data_produk()
        elif pilihan_lihat == '2':
            lihat_data_petani()
        elif pilihan_lihat == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def menu_ubah_data():
    while True:
        print("\nPilihan Ubah Data:")
        print("1. Produk")
        print("2. Petani")
        print("3. Kembali")
        pilihan_ubah = input("Pilih menu: ")
        if pilihan_ubah == '1':
            ubah_data_produk()
        elif pilihan_ubah == '2':
            ubah_data_petani()
        elif pilihan_ubah == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def menu_hapus_data():
    while True:
        print("\nPilihan Hapus Data:")
        print("1. Produk")
        print("2. Petani")
        print("3. Kembali")
        pilihan_hapus = input("Pilih menu: ")
        if pilihan_hapus == '1':
            hapus_data_produk()
        elif pilihan_hapus == '2':
            hapus_data_petani()
        elif pilihan_hapus == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def tambah_data_produk():
    cursor.execute("SELECT MAX(id_produk) FROM produk")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = 0
    id_produk = max_id + 1

    nama_produk = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))

    print("Pilihan Jenis Produk:")
    print("1. Buah-buahan")
    print("2. Sayuran")
    while True:
        choice = input("Masukkan pilihan: ")
        if choice == '1':
            jenis_produk = 'Buah-buahan'
            break
        elif choice == '2':
            jenis_produk = 'Sayuran'
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

    print("Pilihan Metode Produksi:")
    print("1. Pertanian organik")
    print("2. Agroforestry")
    while True:
        choice = input("Masukkan pilihan: ")
        if choice == '1':
            metode_produksi = 'Pertanian organik'
            break
        elif choice == '2':
            metode_produksi = 'Agroforestry'
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

    print("Pilihan Sertifikasi:")
    print("1. Sertifikasi organik")
    print("2. Sertifikasi fair trade")
    print("3. Sertifikasi rainforest alliance")
    while True:
        choice = input("Masukkan pilihan: ")
        if choice == '1':
            sertifikasi = 'Sertifikasi organik'
            break
        elif choice == '2':
            sertifikasi = 'Sertifikasi fair trade'
            break
        elif choice == '3':
            sertifikasi = 'Sertifikasi rainforest alliance'
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

    query = "INSERT INTO produk (id_produk, nama_produk, harga, stok, jenis_produk, metode_produksi, sertifikasi) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id_produk, nama_produk, harga, stok, jenis_produk, metode_produksi, sertifikasi))
    db.commit()
    print("Data produk berhasil ditambahkan.")


def lihat_data_produk():
    while True:
        print("\nPilihan Urutan Data Produk:")
        print("1. Ascending")
        print("2. Descending")
        print("3. Kembali")
        urutan = input("Pilih urutan: ")
        
        if urutan == '1':
            order_by = "ASC"
        elif urutan == '2':
            order_by = "DESC"
        elif urutan == '3':
            return
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            continue

        query = f"SELECT * FROM produk ORDER BY id_produk {order_by}"
        cursor.execute(query)
        results = cursor.fetchall()
        print("Data Produk Pertanian:")
        for row in results:
            print("ID:", row[0])
            print("Nama Produk:", row[2])
            print("Harga:", row[3])
            print("Stok:", row[4])
            print("------------------------")

def ubah_data_produk():
    id_produk = int(input("Masukkan ID produk yang ingin diubah: "))
    nama_produk = input("Masukkan nama produk baru: ")
    harga = float(input("Masukkan harga produk baru: "))
    stok = int(input("Masukkan stok produk baru: "))
    query = "UPDATE produk SET nama_produk = %s, harga = %s, stok = %s WHERE id_produk = %s"
    cursor.execute(query, (nama_produk, harga, stok, id_produk))
    db.commit()
    print("Data produk berhasil diubah.")

def hapus_data_produk():
    id_produk = int(input("Masukkan ID produk yang ingin dihapus: "))
    query = "DELETE FROM produk WHERE id_produk = %s"
    cursor.execute(query, (id_produk,))
    db.commit()
    print("Data produk berhasil dihapus.")

def tambah_data_petani():
    cursor.execute("SELECT MAX(id_petani) FROM petani")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = 0
    id_petani = max_id + 1

    nama_petani = input("Masukkan nama petani: ")
    lokasi_pertanian = input("Masukkan lokasi pertanian: ")
    metode_pertanian = input("Masukkan metode pertanian: ")
    query = "INSERT INTO petani (id_petani, nama_petani, lokasi_pertanian, metode_pertanian) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_petani, nama_petani, lokasi_pertanian, metode_pertanian))
    db.commit()
    print("Data petani berhasil ditambahkan.")

def lihat_data_petani():
    while True:
        print("\nPilihan Urutan Data Petani:")
        print("1. Ascending")
        print("2. Descending")
        print("3. Kembali")
        urutan = input("Pilih urutan: ")
        
        if urutan == '1':
            order_by = "ASC"
        elif urutan == '2':
            order_by = "DESC"
        elif urutan == '3':
            return
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            continue

        query = f"SELECT * FROM petani ORDER BY id_petani {order_by}"
        cursor.execute(query)
        results = cursor.fetchall()
        print("Data Petani:")
        for row in results:
            print("ID:", row[0])
            print("Nama Petani:", row[1])
            print("Lokasi Pertanian:", row[2])
            print("Metode Pertanian:", row[3])
            print("------------------------")

def ubah_data_petani():
    id_petani = int(input("Masukkan ID petani yang ingin diubah: "))
    nama_petani = input("Masukkan nama petani baru: ")
    lokasi_pertanian = input("Masukkan lokasi pertanian baru: ")
    metode_pertanian = input("Masukkan metode pertanian baru: ")
    query = "UPDATE petani SET nama_petani = %s, lokasi_pertanian = %s, metode_pertanian = %s WHERE id_petani = %s"
    cursor.execute(query, (nama_petani, lokasi_pertanian, metode_pertanian, id_petani))
    db.commit()
    print("Data petani berhasil diubah.")

def hapus_data_petani():
    id_petani = int(input("Masukkan ID petani yang ingin dihapus: "))
    query = "DELETE FROM petani WHERE id_petani = %s"
    cursor.execute(query, (id_petani,))
    db.commit()
    print("Data petani berhasil dihapus.")

def sign_up():
    cursor.execute("SELECT MAX(id_user) FROM user")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = 0
    id_user = max_id + 1

    nama_user = input("Masukkan username: ")
    no_telp = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ") 
    alamat = input("Masukkan alamat: ")
    password = getpass("Masukkan password: ")
    verify_password = getpass("Verifikasi password: ")
    if password == verify_password:
        query = "INSERT INTO user (id_user, nama_user, no_telp, email, alamat, password) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id_user, nama_user, no_telp, email, alamat, password))
        db.commit()
        print("Sign up berhasil.")
    else:
        print("Password tidak cocok. Silakan coba lagi.")

def sign_in():
    nama_user = input("Masukkan username: ")
    password = getpass("Masukkan password: ")
    query = "SELECT * FROM user WHERE nama_user = %s AND password = %s"
    cursor.execute(query, (nama_user, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil sebagai user.")
        return True
    else:
        print("Login gagal. Periksa kembali username dan password.")
        return False
    
keranjang = [] 

import mysql.connector

def get_product_name(id_produk):
    try:
        db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kelompok1"
        )

        cursor = db_connection.cursor()

        query = "SELECT nama_produk FROM produk WHERE id = %s"
        cursor.execute(query, (id_produk,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return "Produk tidak ditemukan"

    except mysql.connector.Error as error:
        print("Error:", error)
        return None

    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

id_produk = 1 
nama_produk = get_product_name(id_produk)
print("Nama Produk:", nama_produk)


def beli_produk():
    id_produk = int(input("Masukkan ID produk yang ingin dibeli: "))
    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
    keranjang.append((id_produk, jumlah))
    print("Produk berhasil ditambahkan ke keranjang.")

def lihat_keranjang():
    if keranjang:
        print("Isi Keranjang:")
        for nama_produk, jumlah in keranjang:
            print("Nama Produk:", get_product_name(nama_produk))
            print("Jumlah:", jumlah)
            print("------------------------")
    else:
        print("Keranjang kosong.")


def checkout():
    if not keranjang:
        print("Keranjang kosong. Tidak dapat checkout.")
        return

    print("Pilih metode pembayaran:")
    print("1. Debit Card")
    print("2. Transfer Bank")
    print("3. E-Wallet")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        metode_pembayaran = 'Debit Card'
    elif choice == '2':
        metode_pembayaran = 'Transfer Bank'
    elif choice == '3':
        metode_pembayaran = 'E-Wallet'
    else:
        print("Pilihan tidak valid.")
        return

    for id_produk, jumlah_transaksi in keranjang:
        query = "INSERT INTO transaksi (id_produk, jumlah, metode_pembayaran) VALUES (%s, %s, %s)"
        cursor.execute(query, (id_produk, jumlah_transaksi, metode_pembayaran))
        db.commit()

    print("Pembayaran berhasil dengan", metode_pembayaran)
    keranjang.clear()
    print("Keranjang berhasil dibersihkan.")


def menu_user():
    while True:
        print("\nPilihan Menu User:")
        print("1. Lihat Data Produk Tersedia")
        print("2. Beli Produk")
        print("3. Lihat Isi Keranjang")
        print("4. Checkout")
        print("5. Logout")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            lihat_data_produk()
        elif pilihan == '2':
            beli_produk()
        elif pilihan == '3':
            lihat_keranjang()
        elif pilihan == '4':
            checkout()
        elif pilihan == '5':
            print("Logout berhasil. Sampai jumpa lagi.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def main():
    while True:
        print("\nPilihan Login:")
        print("1. Admin")
        print("2. User Biasa")
        print("3. Keluar")
        pilihan_login = input("Pilih jenis login: ")

        if pilihan_login == '1':
            if login_admin():
                menu_admin()
        elif pilihan_login == '2':
            print("1. Sign In")
            print("2. Sign Up")
            choice = input("Pilih menu: ")
            if choice == '1':
                if sign_in():
                    menu_user()
            elif choice == '2':
                sign_up()
        elif pilihan_login == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
