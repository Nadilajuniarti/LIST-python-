mahasiswa = []
jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"Data ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    alamat = input("Alamat: ")
    mahasiswa.append((nama, nim, alamat))

print("=== DATA MAHASISWA ===")
for nama, nim, alamat in mahasiswa:
    print(f"Nama: {nama}, NIM: {nim}, Alamat: {alamat}")
