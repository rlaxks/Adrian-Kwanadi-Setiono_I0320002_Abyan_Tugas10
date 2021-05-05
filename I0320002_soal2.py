#membuat program biodata
print("Selamat Datang")
print("==============")
print("Silahkan untuk mengisi biodatanya")

#mengambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
jenis_kelamin = input("Jenis Kelamin (L/P): ")
tempat_tanggallahir = input("Tempat dan Tanggal Lahir: ")
alamat = input("Alamat: ")

#format teks
teks = "Nama: {}\nUmur: {}\nJenis Kelamin (L/P): {}\nTempat dan Tanggal Lahir: {}\nAlamat: {}".format(nama, umur, jenis_kelamin, tempat_tanggallahir, alamat)

#membuka file untuk ditulis
file_teks = open("file.txt", "w")

#menulis teks ke file
file_teks.write(teks)

#menutup file
file_teks.close()
