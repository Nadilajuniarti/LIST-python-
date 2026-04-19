#  List Statis

List statis adalah list yang datanya sudah ditentukan langsung di dalam kode.

# Contoh:
buah = ["apel", "jeruk", "mangga"]

for b in buah:
    print(b)


# contoh multi data:
mahasiswa = [
    ("Nadila", "001", "Surabaya"),
    ("Budi", "002", "Malang")
]

for nama, nim, alamat in mahasiswa:
    print(nama, nim, alamat)
