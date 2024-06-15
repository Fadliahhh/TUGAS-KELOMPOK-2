import mysql.connector

# Koneksi ke database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="mydatabase"
    )

# Create data
def create_person(nama, tempat_lahir):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO data_orang (nama, tempat_lahir) VALUES (%s, %s)"
    cursor.execute(query, (nama, tempat_lahir))
    conn.commit()
    conn.close()

# Read data
def read_data():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM data_orang"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Update data
def update_data(data_id, nama, tempat_lahir):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE data_orang SET nama = %s, tempat_lahir = %s WHERE id = %s"
    cursor.execute(query, (nama, tempat_lahir, data_id))
    conn.commit()
    conn.close()

# Delete data
def delete_data(data_id):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM data_orang WHERE id = %s"
    cursor.execute(query, (data_id,))
    conn.commit()
    conn.close()

# Search data
def cari_data(nama):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM data_orang WHERE nama LIKE %s"
    cursor.execute(query, (f"%{nama}%",))
    results = cursor.fetchall()
    conn.close()
    return results

# Main program
if __name__ == "__main__":
    while True:
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Ubah data")
        print("4. Hapus data")
        print("5. Cari data")
        print("6. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            nama = input("Masukkan nama: ")
            tempat_lahir = input("Masukkan tempat lahir: ")
            create_person(nama, tempat_lahir)
        elif choice == '2':
            data_orang = read_data()
            for orang in data_orang:
                print(f"ID: {orang[0]}, Nama: {orang[1]}, Tempat Lahir: {orang[2]}")
        elif choice == '3':
            id_orang = int(input("Masukkan ID: "))
            nama = input("Masukkan nama baru: ")
            tempat_lahir = input("Masukkan tempat lahir baru: ")
            update_data(id_orang, nama, tempat_lahir)
        elif choice == '4':
            id_orang = int(input("Masukkan ID: "))
            delete_data(id_orang)
        elif choice == '5':
            nama = input("Masukkan nama yang dicari: ")
            persons = cari_data(nama)
            for orang in persons:
                print(f"ID: {orang[0]}, Nama: {orang[1]}, Tempat Lahir: {orang[2]}")
        elif choice == '6':
            break
        else:
            print("Opsi tidak valid!")
