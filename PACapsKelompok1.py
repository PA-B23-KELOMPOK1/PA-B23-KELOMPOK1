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
        print("1. Tambah data produk")
        print("2. Lihat data produk")
        print("3. Ubah data produk")
        print("4. Hapus data produk")
        print("5. Tambah data petani")
        print("6. Lihat data petani")
        print("7. Ubah data petani")
        print("8. Hapus data petani")
        print("9. Logout")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tambah_data_produk()
        elif pilihan == '2':
            lihat_data_produk()
        elif pilihan == '3':
            ubah_data_produk()
        elif pilihan == '4':
            hapus_data_produk()
        elif pilihan == '5':
            tambah_data_petani()
        elif pilihan == '6':
            lihat_data_petani()
        elif pilihan == '7':
            ubah_data_petani()
        elif pilihan == '8':
            hapus_data_petani()
        elif pilihan == '9':
            print("Logout berhasil.")
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
    query = "INSERT INTO produk (id_produk, nama_produk, harga, stok) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_produk, nama_produk, harga, stok))
    db.commit()
    print("Data produk berhasil ditambahkan.")


def lihat_data_produk():
    query = "SELECT * FROM produk"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Data Produk Pertanian:")
    for row in results:
        print("ID:", row[0])
        print("Nama Produk:", row[1])
        print("Harga:", row[2])
        print("Stok:", row[3])
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
    query = "SELECT * FROM petani"
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
    nama_user = input("Masukkan username: ")
    no_telp = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ") 
    alamat = input("Masukkan alamat: ")
    password = getpass("Masukkan password: ")
    verify_password = getpass("Verifikasi password: ")
    if password == verify_password:
        query = "INSERT INTO user (nama_user, no_telp, email, alamat, password) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nama_user, no_telp, email, alamat, password))
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
    
def beli_produk():
    id_produk = int(input("Masukkan ID produk yang ingin dibeli: "))
    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
    query = "INSERT INTO transaksi (id_produk, jumlah) VALUES (%s, %s)"
    cursor.execute(query, (id_produk, jumlah))
    db.commit()
    print("Produk berhasil ditambahkan ke keranjang.")

def lihat_keranjang():
    query = "SELECT produk.nama_produk, transaksi.jumlah FROM transaksi JOIN produk ON transaksi.id_produk = produk.id"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("Isi Keranjang:")
        for row in results:
            print("Nama Produk:", row[0])
            print("Jumlah:", row[1])
            print("------------------------")
    else:
        print("Keranjang kosong.")

def checkout():
    # Implementasikan logika checkout
    metode_pembayaran = input("Pilih metode pembayaran (Cash / Debit Card): ")
    if metode_pembayaran.lower() == 'cash' or metode_pembayaran.lower() == 'debit card':
        print("Pembayaran berhasil dengan", metode_pembayaran)
        query = "DELETE FROM transaksi"
        cursor.execute(query)
        db.commit()
        print("Keranjang berhasil dibersihkan.")
    else:
        print("Metode pembayaran tidak valid.")

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
