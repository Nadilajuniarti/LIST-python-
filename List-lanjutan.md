#  List Lanjutan
penggunaan list lebih lanjut

# Nested List (List di dalam List)
Nested list adalah list yang berisi list lain di dalamnya.
Biasanya digunakan untuk menyimpan data berkelompok.

# Contoh Program: 
data = [
    ["Nadila", "001"],
    ["Budi", "002"]
]

for d in data:
    print("Nama:", d[0], "NIM:", d[1])

📌 Tuple dalam List
Tuple dalam list digunakan untuk menyimpan beberapa data dalam satu paket. Biasanya digunakan untuk data yang tidak ingin diubah.

# Contoh Program:
data = [
    ("Nadila", "001"),
    ("Budi", "002")
]

for nama, nim in data:
    print("Nama:", nama, "NIM:", nim)

📌 Unpacking (Tanpa Index)
Unpacking adalah cara mengambil isi data tanpa menggunakan index. Data langsung dimasukkan ke variabel.

# Contoh Program:
data = [("dila", 17), ("mimi", 22)]

for nama, umur in data:
    print(nama, umur)

📌 Cek Data dalam List
Digunakan untuk mengecek apakah suatu data ada di dalam list.

# Contoh Program:
nama = ["andi", "budi", "caca"]

if "budi" in nama:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

