#  List Dinamis
List dinamis adalah list yang datanya diinput oleh pengguna/user saat program dijalankan.

# Contoh:

data = []
jumlah = int(input("Jumlah data: "))

for i in range(jumlah):
    nama = input("Masukkan data: ")
    data.append(nama)

print(data)

# contoh multi data:

mahasigma = []
jumlah = int(input("masukkan jumlah mahasigma: "))
for i in range(jumlah):
    print(f"DATA KE-{i+1}")
    nama = input("masukkan nama: ")
    kelas = input("masukkan kelas: ")
    mahasigma.append((nama,kelas))

print("==data mahasgma==")
for nama,kelas in mahasigma:
    print(nama,kelas)
