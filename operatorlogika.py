#SOAL 1
nama_user = input("Masukan nama anda : ")
password_user = input("Masukan Password anda : ")

nama = "Adrian PC"
password = "adrian124"

if((nama_user == nama) & (password_user == password)):
    print("Selamat datang Admin")

else:
    print("Nama atau password yang anda masukan salah")

#SOAL 2
umur =int(input("Masukan Umur anda"))
keanggotaan_aktif = input("apakah anda aktif berolahraga ( yes / no ")
keanggotaan = False

if (keanggotaan_aktif == "yes") :
    keanggotaan = False
else:
    keanggotaan= True

if(umur > 18) and (keanggotaan == True):
    print("Selamat datang di Klub Olahraga Kami")

else:
    print("Anda Belum bisa Masuk ke klub olahraga kami")

#SOAL 3
umur=int(input("Masukan umur anda") 
status_anda=input("Masukan statuss and")

staatu="Pelajar"
status2="Anggota film klub"

if umur < 18:
   if (status_anda == statuss or status2):
       print("Andaa memenuhi syarat diskon pelajar")
 else:
     print ("Anda tidak memenuhi syarat diskon pelajaar")
