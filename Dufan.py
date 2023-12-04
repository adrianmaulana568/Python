print("Selamat datang di dafun")
nama=input("Masukan Nama :")
umur=input("Masukan umur mu :")

print("Haloo", nama, "Selamat menikmati wahana di dafun")
total_pembelian=0
harga_wahana=[13000,10000,15000,20000]

print("Daftar Wahana")
print("Bilang lala RP. 13.000")
print("Istana boneka RP. 10.000")
print("Rumah kaca RP. 15.000")
print("Roller coaster RP. 20.000")

wahana=int(input("Masukan Wahana"))
if(wahana <0):
    print("input pilihan anda tidak bole kurang dari 0")
elif (wahana> len(harga_wahana)):
    print("Input yang anda perintahkan tidak ada dalam daftar wahana")
else:
    total_pembelian +=harga_wahana[wahana -1]
    print("Harga tiket wahana :  ",total_pembelian)
    pajak = 2000
    total_pembelian += pajak
    print("Total keseluruhan",total_pembelian)
