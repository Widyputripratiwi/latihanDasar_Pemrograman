nama = "Widy Putri Pratiwi"
alamat = "Jl. Pelabuhan II No 14, Cikembar, Sukabumi"

print("Nama Saya :", nama)
print("Alamat Saya :", alamat)
# ambil string berdasarkan index
print("Huruf pertama nama Saya :", nama [0])
print("Huruf terakhir nama Saya :", nama [-1])
print("Nama terakhir nama Saya :", nama [-7:])
print("Nama depan nama Saya :", nama [:-14])



# split string menjadi array
alamat_array = alamat.split(', ')
jalan = alamat_array[0]
kecamatan = alamat_array[1]
kabupaten = alamat_array[2]

print("Alamat saya array ", alamat_array)
print("alamat jalan saya :", jalan)
print("alamat kecamatan saya :", kecamatan)
print("alamat kabupaten saya :", kabupaten)
print("saya tinggal di ", jalan, "Kecamatan", kecamatan, "Kabupaten", kabupaten)

print(f'saya tinggal di {jalan} Kecamatan {kecamatan} kabupaten {kabupaten}')

#join string
pemisah = "@"
print("alamat join saya :", pemisah.join (alamat_array ))
