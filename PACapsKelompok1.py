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
    linked_list = LinkedList()
    while True:
        print("\nPilihan Menu Admin:")
        print("1. Tambah data")
        print("2. Lihat data (Sorting Ascending dan Descending)")
        print("3. Ubah data")
        print("4. Hapus data")
        print("5. Cari Produk")
        print("6. Logout")
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
            cari_produk()
        elif pilihan == '6':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def tambah_data_produk():
    nama_produk = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))
    query = "INSERT INTO produk (nama_produk, harga, stok) VALUES (%s, %s, %s)"
    cursor.execute(query, (nama_produk, harga, stok))
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
    query = "UPDATE produk SET nama_produk = %s, harga = %s, stok = %s WHERE id = %s"
    cursor.execute(query, (nama_produk, harga, stok, id_produk))
    db.commit()
    print("Data produk berhasil diubah.")

def hapus_data_produk():
    id_produk = int(input("Masukkan ID produk yang ingin dihapus: "))
    query = "DELETE FROM produk WHERE id = %s"
    cursor.execute(query, (id_produk,))
    db.commit()
    print("Data produk berhasil dihapus.")

def cari_produk():
    keyword = input("Masukkan nama produk yang ingin dicari: ")
    query = "SELECT * FROM produk WHERE nama_produk LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    results = cursor.fetchall()
    if results:
        print("Hasil Pencarian:")
        for row in results:
            print("ID:", row[0])
            print("Nama Produk:", row[1])
            print("Harga:", row[2])
            print("Stok:", row[3])
            print("------------------------")
    else:
        print("Produk tidak ditemukan.")

def sign_up():
    nama_user = input("Masukkan username: ")
    no_telp = input("Masukkan nomor telepon: ")
    password = getpass("Masukkan password: ")
    verify_password = getpass("Verifikasi password: ")
    if password == verify_password:
        query = "INSERT INTO user (nama_user, no_telp, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (nama_user, no_telp, password))
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
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# # Fungsi untuk beli produk
# def beli_produk():
#     id_produk = int(input("Masukkan ID produk yang ingin dibeli: "))
#     jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
#     # Implementasikan logika beli produk
#     # Misalnya, tambahkan data transaksi ke database
#     print("Produk berhasil ditambahkan ke keranjang.")

# # Fungsi untuk lihat isi keranjang
# def lihat_keranjang():
#     # Implementasikan logika lihat isi keranjang
#     # Misalnya, tampilkan produk-produk yang telah ditambahkan ke keranjang
#     print("Isi Keranjang:")
#     # Implementasi sesuai dengan struktur keranjang yang Anda inginkan

# # Fungsi untuk checkout
# def checkout():
#     # Implementasikan logika checkout
#     # Misalnya, lakukan pembayaran dan update status transaksi
#     metode_pembayaran = input("Pilih metode pembayaran (Cash / Debit Card): ")
#     if metode_pembayaran.lower() == 'cash':
#         print("Pembayaran berhasil dengan tunai.")
#     elif metode_pembayaran.lower() == 'debit card':
#         print("Pembayaran berhasil dengan kartu debit.")
#     else:
#         print("Metode pembayaran tidak valid.")

    # Setelah pembayaran berhasil, lakukan penanganan transaksi, seperti update status atau hapus keranjang
    # Misalnya, implementasikan logika untuk menghapus produk dari keranjang atau menambahkan transaksi ke database



# Program Utama
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
            sign_in()
            menu_user()
        elif pilihan_login == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
